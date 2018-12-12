import subprocess, re

def ping():
    P = subprocess.Popen("ping google.com", stderr=subprocess.PIPE, stdout=subprocess.PIPE)
    out, err = P.communicate()
    return out

def parserAvr(out):
    patternAvr = r"(Average.*)(.*?\d+)"
    analyzeAvr = re.search(patternAvr, out)
    avr = analyzeAvr.group(2)
    return str(avr)

def parserRec(out):
    patternRec = r"(Received .*?\S)(.*?\d+)"
    analyzeRec = re.search(patternRec, out)
    rec = analyzeRec.group(2)
    return int(rec)
"""
if __name__ == "__main__":
    out, err = ping()
    print parserAvr(out)
"""