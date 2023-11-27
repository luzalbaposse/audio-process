import os
import subprocess

def convert_m4a_to_wav(input_folder):
    for root, dirs, files in os.walk(input_folder):
        if "WAV" in dirs:
            continue

        for file in files:
            if file.endswith(".m4a"):
                input_path = os.path.join(root, file)
                output_folder = os.path.join(root, "WAV")
                os.makedirs(output_folder, exist_ok=True)
                output_path = os.path.join(output_folder, os.path.splitext(file)[0] + ".wav")
                
                # Run the ffmpeg command
                command = f"ffmpeg -i {input_path} -ar 16000 {output_path}"
                subprocess.run(command, shell=True)

if __name__ == "__main__":
    directory_path = input("Enter the directory path: ")
    convert_m4a_to_wav(directory_path)
