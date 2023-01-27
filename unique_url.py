import concurrent.futures
import sys

def get_param(url):
    if "?" not in url or "=" not in url:
        return None
    param = url.split("?")[1].split("=")[0]
    return param

def process_chunk(chunk):
    unique_params = set()
    unique_urls = []
    for url in chunk:
        param = get_param(url)
        if param not in unique_params:
            unique_params.add(param)
            unique_urls.append(url)
    return unique_urls

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 script.py file.txt")
        sys.exit()
    file = sys.argv[1]
    with open(file, "r") as f:
        urls = f.readlines()
    urls = [url.strip() for url in urls]
    chunk_size = int(len(urls) / 4)
    chunks = [urls[i:i+chunk_size] for i in range(0, len(urls), chunk_size)]
    with concurrent.futures.ProcessPoolExecutor() as executor:
        results = [executor.submit(process_chunk, chunk) for chunk in chunks]
    unique_urls = []
    for future in concurrent.futures.as_completed(results):
        unique_urls += future.result()
    with open("unique_urls.txt", "w") as f:
        for url in unique_urls:
            f.write(url + "\n")

if __name__ == "__main__":
    main()
