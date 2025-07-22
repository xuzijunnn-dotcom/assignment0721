import os
import random
from pydub import AudioSegment
import traceback

input_folder = "/Users/xuzijun/Desktop/Working/Summer/pangloss_sample"
output_folder = "new_audio_files"
os.makedirs(output_folder, exist_ok=True)

codebook = []
count = 1

def to_be_extracted_clip(audio, duration_ms):
    duration_ms = min(duration_ms, len(audio))
    start = random.randint(0, len(audio) - duration_ms)
    return audio[start:start+duration_ms]

for filename in os.listdir(input_folder):
        
    full_path = os.path.join(input_folder, filename)
    
    try:
        audio = AudioSegment.from_mp3(full_path)
        duration_sec = len(audio) / 1000  
        
        if duration_sec < 10:
            print(f"⭕️ {filename} - too short ({duration_sec:.2f} seconds)")
            continue

        print(f"✅ {filename} - {duration_sec:.2f} seconds")

        for i in range(5):
            clip = to_be_extracted_clip(audio, 10*1000)  
            name = f"{count:02d}.wav"
            save_path = os.path.join(output_folder, name)
            clip.export(save_path, format="wav")
            codebook.append((name, filename))
            count += 1
            
    except Exception as e:
        print(f"❌ Failed to process {filename}: {str(e)}")
        traceback.print_exc()
with open("codebook.txt", "w") as f:
    for anon_name, original_name in codebook:
        f.write(f"{anon_name} --> {original_name}\n")

if os.path.exists("codebook.txt"):
    print("📄 Codebook successfully created: codebook.txt")

