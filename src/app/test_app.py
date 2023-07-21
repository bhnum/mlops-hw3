import time
import requests

def test_latency():
    start_time = time.time()
    image_path = "../images/car.jpg"

    with open(image_path, "rb") as file:
        files = {"image": file}
        response = requests.post("http://localhost:8000/predict", files=files)

    assert response.status_code == 200
    end_time = time.time()
    latency = end_time - start_time
    print(f"Latency: {latency} seconds")

if __name__ == "__main__":
    test_latency()
