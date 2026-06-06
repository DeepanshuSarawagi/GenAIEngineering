"""pandas_lab.py

Download a CSV from a public URL and load it into a pandas DataFrame.
This version is synchronous and works in a normal Python environment (no Pyodide).
The code will try to use `requests` if available, otherwise fall back to the standard
library `urllib.request`.
"""
import sys
from pathlib import Path
import pandas as pd

URL = (
    "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/"
    "LXjSAttmoxJfEG6il1Bqfw/Product-sales.csv"
)


def download_with_requests(url: str, out_path: Path) -> None:
    """Download using requests (streaming)."""
    import requests

    resp = requests.get(url, stream=True, timeout=30)
    resp.raise_for_status()
    with out_path.open("wb") as f:
        for chunk in resp.iter_content(chunk_size=8192):
            if chunk:
                f.write(chunk)


def download_with_urllib(url: str, out_path: Path) -> None:
    """Fallback download using urllib (stdlib)."""
    import urllib.request
    import ssl

    try:
        with urllib.request.urlopen(url, timeout=30) as resp:
            if getattr(resp, "status", 200) != 200:
                raise RuntimeError(f"Download failed, HTTP status: {getattr(resp, 'status', 'unknown')}")
            data = resp.read()
            out_path.write_bytes(data)
    except Exception as e:
        # Some environments raise a URLError wrapping an SSL error. If the failure
        # appears to be a certificate verification problem, retry without verification.
        msg = str(e)
        if isinstance(e, ssl.SSLError) or "CERTIFICATE_VERIFY_FAILED" in msg or "ssl" in msg.lower():
            ctx = ssl.create_default_context()
            ctx.check_hostname = False
            ctx.verify_mode = ssl.CERT_NONE
            with urllib.request.urlopen(url, context=ctx, timeout=30) as resp:
                if getattr(resp, "status", 200) != 200:
                    raise RuntimeError(f"Download failed, HTTP status: {getattr(resp, 'status', 'unknown')}")
                out_path.write_bytes(resp.read())
        else:
            raise


def download(url: str, out_path: Path) -> None:
    """Try to download using requests, otherwise use urllib."""
    try:
        download_with_requests(url, out_path)
    except Exception:
        # If requests not available or download fails, fall back to urllib
        download_with_urllib(url, out_path)


def main():
    out_file = Path(__file__).with_name("Product-sales.csv")
    print(f"Downloading {URL} -> {out_file}")
    try:
        download(URL, out_file)
    except Exception as e:
        print("Download failed:", e, file=sys.stderr)
        sys.exit(1)

    print("Reading CSV into pandas DataFrame...")
    df = pd.read_csv(out_file)
    print("First 5 rows:")
    print(df.head())


if __name__ == "__main__":
    main()
