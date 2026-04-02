# PYTHON ISBN API (Flask) BY ANGELA GLADYS
## Features
- Compute ISBN-10 check digit
- Validating ISBN-10
- Converting ISBN-10 to ISBN-13
- Validating ISBN-13

## Endpoints

### 1. Compute Check Digit
POST /isbn10/check-digit

### 2. Validate ISBN-10
POST /isbn10/validate

### 3. Convert ISBN-10 → ISBN-13
POST /isbn10/to-isbn13

### 4. Validate ISBN-13
POST /isbn13/validate

## Example Request

```json
{
  "isbn": "0306406152"
}
