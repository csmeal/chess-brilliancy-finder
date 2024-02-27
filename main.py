import subprocess
from dotenv import load_dotenv
import os


load_dotenv()

def interact_with_external_app(fen):
    # Start the external application
    app_process = subprocess.Popen([os.getenv("STOCKFISH_PATH")], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

    # Send a command to the application
    setup_ffn(app_process, fen)

    # Read the output of the application
    wait_for_pos(app_process, "e1e8")
 
 
def send_command(app, command):
    app.stdin.write(command + "\n")
    app.stdin.flush()

def wait_for_pos(app, pos):
    print('here we go')
    send_command(app, "go infinite")

   
    counter = 0
    for eline in iter(app.stdout.readline, ''):
        parse_line(eline)
        print(eline)
        if counter > 50:
            break
        counter += 1
def parse_eval_line(line):
    pass
def parse_line(line):
    if line.startswith("info depth"):
        print(parse_info_line(line))
def parse_info_line(line):
    print('parsing info')
    words = line.split(' ')
    if "pv" in words:
        move = words[words.index('pv')+1]
    if "cp" in words:
        evaluation = int(words[words.index('cp')+1])
        print(f"current eval: {evaluation}")
    elif "mate" in words:
        evaluation = int(words[words.index('mate')+1])
        print(f" mate in {evaluation}")
    return {"e": evaluation, "mv": move}
   
   
   
def setup_ffn(app, ffn):
    send_command(app, 'position startpos')
    send_command(app, f'position fen {ffn}')
    app.stdin.flush()
   
if __name__ == "__main__":
    #interact_with_external_app("8/8/4kpp1/3p1b2/p6P/2B5/6P1/6K1 b - - 0 47")
    #interact_with_external_app("k7/pp6/8/8/8/8/8/K3R3 w - - 0 1")
    interact_with_external_app("n1QBq1k1/5p1p/5KP1/p7/8/8/8/8 w - - 0 1")