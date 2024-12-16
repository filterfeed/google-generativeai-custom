
# Google GenerativeAI Custom

A customized version of the Google GenerativeAI library that increases the API timeout, enabling support for longer-running requests without interruptions.

## Features

- Extends the standard API timeout for GenerativeAI requests.
- Supports longer-running operations, ensuring stability for resource-intensive tasks.

## Installation

To install the custom library directly from this repository:

```bash
pip install git+https://github.com/filterfeed/google-generativeai-custom.git@main#egg=google-generativeai-custom
```

## Usage

Import and use the library just like the standard `google.generativeai` module:

```python
import google.generativeai as genai

# Example usage
model = genai.GenerativeModel("gemini-pro")
response = model.generate_content("Tell me a story about space exploration.")
print(response.text)
```

## Custom Timeout Configuration

The extended timeout allows requests to run longer without being prematurely terminated. Ideal for processing tasks that require more time to complete.

## Contributing

Contributions are welcome! To add improvements or fixes:

1. Fork the repository.
2. Create a new branch: `git checkout -b feature/your-feature`.
3. Commit your changes: `git commit -m "Add your feature"`.
4. Push the branch: `git push origin feature/your-feature`.
5. Open a Pull Request.

## License

This project is licensed under the MIT License.
