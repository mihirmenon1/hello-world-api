from fastapi import FastAPI, HTTPException
import math

app = FastAPI()


@app.get("/")
def root():
    """
    Root route that returns a welcome message.
    Returns a static JSON message confirming the API is running.
    """
    return {"message": "Hello, World!"}


@app.get("/hello/{name}")
def hello(name: str):
    """
    Greeting returns message.
    Takes a name as input and returns greeting.
    """
    return {"message": f"Hello, {name}!"}


@app.get("/add/{a}/{b}")
def add(a: float, b: float):
    """
    Adds two numbers together.
    Accepts two float path parameters a and b.
    Returns the sum as a JSON response with the operation name, inputs, and result.
    Example: /add/4/7.5 returns {"operation": "add", "a": 4.0, "b": 7.5, "result": 11.5}
    """
    if math.isnan(a) or math.isnan(b):
        raise HTTPException(status_code=422, detail="All arguments must be valid numbers.")
    return {"operation": "add", "a": a, "b": b, "result": a + b}


@app.get("/subtract/{a}/{b}")
def subtract(a: float, b: float):
    """
    Subtracts b from a.
    Accepts two float path parameters a and b.
    Returns the difference as a JSON response with the operation name, inputs, and result.
    Example: /subtract/10/3 returns {"operation": "subtract", "a": 10.0, "b": 3.0, "result": 7.0}
    """
    if math.isnan(a) or math.isnan(b):
        raise HTTPException(status_code=422, detail="All arguments must be valid numbers.")
    return {"operation": "subtract", "a": a, "b": b, "result": a - b}


@app.get("/multiply/{a}/{b}")
def multiply(a: float, b: float):
    """
    Multiplies two numbers together.
    Accepts two float path parameters a and b.
    Returns the product as a JSON response with the operation name, inputs, and result.
    Example: /multiply/3/4 returns {"operation": "multiply", "a": 3.0, "b": 4.0, "result": 12.0}
    """
    if math.isnan(a) or math.isnan(b):
        raise HTTPException(status_code=422, detail="All arguments must be valid numbers.")
    return {"operation": "multiply", "a": a, "b": b, "result": a * b}


@app.get("/divide/{a}/{b}")
def divide(a: float, b: float):
    """
    Divides a by b.
    Accepts two float path parameters a and b.
    Returns the quotient as a JSON response with the operation name, inputs, and result.
    Returns a 422 error if b is zero.
    Example: /divide/10/2 returns {"operation": "divide", "a": 10.0, "b": 2.0, "result": 5.0}
    """
    if math.isnan(a) or math.isnan(b):
        raise HTTPException(status_code=422, detail="All arguments must be valid numbers.")
    if b == 0:
        raise HTTPException(status_code=422, detail="Division by zero is not allowed. Please provide a non-zero value for b.")
    return {"operation": "divide", "a": a, "b": b, "result": a / b}


@app.get("/tip/{bill}/{percentage}")
def tip(bill: float, percentage: float):
    """
    Calculates the tip amount for a given bill and tip percentage.
    Accepts two float path parameters: bill (total bill amount) and percentage (tip percent).
    Returns the tip amount and total bill with tip included.
    Bill and percentage must be positive numbers.

    """
    if math.isnan(bill) or math.isnan(percentage):
        raise HTTPException(status_code=422, detail="All arguments must be valid numbers.")
    if bill < 0:
        raise HTTPException(status_code=422, detail="Bill amount must be a positive number.")
    if percentage < 0:
        raise HTTPException(status_code=422, detail="Tip percentage must be a positive number.")
    tip_amount = round(bill * (percentage / 100), 2)
    total = round(bill + tip_amount, 2)
    return {"operation": "tip", "bill": bill, "percentage": percentage, "tip_amount": tip_amount, "total": total}


@app.get("/discount/{price}/{percent_off}")
def discount(price: float, percent_off: float):
    """
    Calculates the discounted price after applying a percentage discount.
    Accepts two float path parameters: price (original price) and percent_off (discount percentage).
    Price must be positive and percent_off must be between 0 and 100.
   
    """
    if math.isnan(price) or math.isnan(percent_off):
        raise HTTPException(status_code=422, detail="All arguments must be valid numbers.")
    if price < 0:
        raise HTTPException(status_code=422, detail="Price must be a positive number.")
    if percent_off < 0 or percent_off > 100:
        raise HTTPException(status_code=422, detail="Discount percentage must be between 0 and 100.")
    savings = round(price * (percent_off / 100), 2)
    discounted_price = round(price - savings, 2)
    return {"operation": "discount", "original_price": price, "percent_off": percent_off, "savings": savings, "discounted_price": discounted_price}


@app.get("/fuel-cost/{miles}/{mpg}/{price_per_gallon}")
def fuel_cost(miles: float, mpg: float, price_per_gallon: float):
    """
    Calculates the total fuel cost for a trip.
    Accepts three float path parameters: miles (distance of trip), mpg (miles per gallon of vehicle),
    and price_per_gallon (cost of fuel per gallon).
    All values must be positive. mpg cannot be zero.
   
    """
    if math.isnan(miles) or math.isnan(mpg) or math.isnan(price_per_gallon):
        raise HTTPException(status_code=422, detail="All arguments must be valid numbers.")
    if miles < 0 or price_per_gallon < 0:
        raise HTTPException(status_code=422, detail="Miles and price per gallon must be positive numbers.")
    if mpg <= 0:
        raise HTTPException(status_code=422, detail="MPG must be a positive number greater than zero.")
    gallons_needed = round(miles / mpg, 2)
    total_cost = round(gallons_needed * price_per_gallon, 2)
    return {"operation": "fuel-cost", "miles": miles, "mpg": mpg, "price_per_gallon": price_per_gallon, "gallons_needed": gallons_needed, "total_cost": total_cost}