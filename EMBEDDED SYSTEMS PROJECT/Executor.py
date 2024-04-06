import subprocess

programs = ["checkA.py", "checkB.py",  "checkC.py", "checkE.py"]

for program in programs:
    try:
        subprocess.run(["python", program], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error running {program}: {e}")

print("All programs executed.")
