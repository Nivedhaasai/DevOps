# Docker Setup

This is the house price model from my earlier mlflow lab, now put behind a
simple API and packed into a docker image.

## 1. Build the Docker Image

```bash
docker build -t nivedhaasai/house_price_regression:latest .
```

---

## 2. Run the Docker Container

```bash
docker run -p 8000:8000 nivedhaasai/house_price_regression:latest
```

The API will now be available at

```
http://localhost:8000
```

---

## 3. Push the Image to Docker Hub

Login to Docker Hub

```bash
docker login
```

Push the image

```bash
docker push nivedhaasai/house_price_regression:latest
```

---

## 4. Pull the Image

Anyone can pull the image using

```bash
docker pull nivedhaasai/house_price_regression:latest
```

---

## 5. Run the Pulled Image

```bash
docker run -p 8000:8000 nivedhaasai/house_price_regression:latest
```

---

# API Endpoints

## Home

**GET**

```
/
```

---

## Health Check

**GET**

```
/health
```

Response

```json
{
    "status": "ok"
}
```

---

## Prediction

**POST**

```
/predict
```

Request

The features are, in this order:
`MedInc, HouseAge, AveRooms, AveBedrms, Population, AveOccup, Latitude, Longitude`

```json
{
    "features": [
        1.6812,
        25.0,
        4.1922,
        1.0223,
        1392.0,
        3.8774,
        36.06,
        -119.01
    ]
}
```

Example Response

```json
{
    "predicted_price": 0.5593,
    "unit": "100,000 USD",
    "features_used": [
        "MedInc",
        "HouseAge",
        "AveRooms",
        "AveBedrms",
        "Population",
        "AveOccup",
        "Latitude",
        "Longitude"
    ]
}
```

---

# Docker Hub Repository

```
https://hub.docker.com/r/nivedhaasai/house_price_regression
```

---
