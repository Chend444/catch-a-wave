# catch-a-wave

**RestAPI** which provides real-time suggestions about where you would wanna go to catch the best waves

## Overview

The **Catch-A-Wave** project aims to deliver real-time suggestions for surfing enthusiasts, offering insights into the best locations to catch the most favorable waves.

### External APIs Used

- **WeatherAPI**: The project utilizes the [WeatherAPI](http://api.weatherapi.com) to gather real-time weather data, which helps in suggesting optimal surfing locations.

### Technologies Used

- **Flask**: Framework used to build the RESTful API.
- **Redis**: Database used for caching and storing weather data.

## Setup Instructions

To set up the project locally, follow these steps:

1. **Clone the repository**:

    ```bash
    git clone https://github.com/Chend444/catch-a-wave.git
    ```

2. **Install the required dependencies**:

    ```bash
    pip install -r requirements.txt
    ```

3. **Set up environment variables**:

    - Provide your WeatherAPI key in the `config.py` file.

4. **Run the application**:

    ```bash
    python app.py
    ```

## API Endpoints

- `/marine/city/waves/range/<cityName>` (GET): Provides wave range suggestions for a given city.
- `/marine/city/waves/peak/<cityName>` (GET): Offers peak hour suggestions for waves in a specific city.

## Contributing

Contributions are welcome! Feel free to open an issue or create a pull request.

## License

This project is licensed under the [MIT License](LICENSE).
