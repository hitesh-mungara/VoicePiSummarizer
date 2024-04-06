                        Meeting Synopsis Generator

Project Description
The Meeting Synopsis Generator is designed for recording and summarizing meetings in real-time using an embedded board. This project captures and transcribes discussions, generating a concise meeting report that is then uploaded to the cloud.

Installation
Before running the project locally, make sure to install the required libraries using the following commands:
pip install pydub
pip install pyaudio
sudo apt-get install portaudio19-dev
pip install tensorflow
pip install tensorflow-io
pip install transformers
pip install librosa
pip install summarizer
pip install keyboard

Additionally, we need to import the required Machine Learning models using the following commands:
transformers-cli login
transformers-cli repo login
transformers-cli repo fetch openai/whisper-tiny.en



Usage
To use the Meeting Synopsis Generator, follow these simple steps:

Load the provided zip file onto the SD card.
Open the file in Thonny IDE through the Microprocessor.
Start the program by executing "Executor.py".
This single program runs the entire application, utilizing parallelization through multi-threading. Threads are allocated to A.py and B.py, executing simultaneously. Note that B.py relies on the output of A.py, and C.py derives its input from the output of B.py.

Features
Machine Learning: The project employs machine learning techniques for efficient synopsis generation, utilizing separate models for Speech-to-Text and Text-to-Summary report.

Multi-Threading: Leveraging parallelization through multi-threading ensures optimal resource utilization and minimal execution time.

Minimal-resource Intensive Execution: The application efficiently solves the problem using just a Microboard.

Contributing
We welcome contributions to enhance the Meeting Synopsis Generator, especially in the following areas:

Voice Identification Integration: Integrate voice identification to generate individual reports for each participant in the meeting.

Model Optimization: Refine model parameters to reduce runtime while maintaining consistent accuracy.

Feel free to fork the repository, make your improvements, and submit a pull request.
Contact Information
For questions or collaboration opportunities, feel free to reach out to:
Shenthan Marru ~ shenthan100s@gmail.com
Yellina Sri Bhargav ~ bhargavyellina@gmail.com
Lakshman Goutham ~ vlak863@gmail.com
Hitesh Mungara ~  hiteshmungara012@gmail.com
