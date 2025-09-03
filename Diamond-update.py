import os, sys, time, random

# ---------- Colors ----------
R='\033[1;31m'; G='\033[1;32m'; Y='\033[1;33m'; B='\033[1;34m'
C='\033[1;36m'; M='\033[1;35m'; W='\033[1;37m'; K='\033[90m'
RESET='\033[0m'

# ---------- Utils ----------
def clear(): os.system('clear' if os.name!='nt' else 'cls')

def typewrite(text, delay=0.007):
    for ch in text:
        sys.stdout.write(ch); sys.stdout.flush(); time.sleep(delay)
    print()

def spinner(title, secs=2.2):
    frames=['⠋','⠙','⠸','⠴','⠦','⠇']
    sys.stdout.write(Y+title+" "+RESET)
    t0=time.time(); i=0
    while time.time()-t0<secs:
        sys.stdout.write(M+frames[i%len(frames)]+RESET); sys.stdout.flush()
        time.sleep(0.12); sys.stdout.write('\b'); i+=1
    print(G+"✓"+RESET)

def progress_bar(title, width=36, duration=1.8):
    print(C+title+RESET)
    steps=max(1,int(duration/0.04))
    for i in range(steps+1):
        fill=int(i/steps*width)
        bar=G+"█"*fill+RESET+"░"*(width-fill)
        pct=int(i/steps*100)
        sys.stdout.write(M+f"[{bar}] {pct:3d}%\r"+RESET); sys.stdout.flush()
        time.sleep(0.04)
    print()

def wave_line(cols=58, rows=3):
    pat=['▁','▂','▃','▄','▅','▆','▇','█','▇','▆','▅','▄','▃','▂']
    for _ in range(rows):
        row="".join(random.choice([G,Y,C,M]) + random.choice(pat) + RESET for _ in range(cols))
        print(row); time.sleep(0.02)

def confetti(lines=3, width=60):
    syms=['✦','✧','✪','✺','✹','✱','✲']; cols=[R,G,Y,B,C,M,W]
    for _ in range(lines):
        print("".join(random.choice(cols)+random.choice(syms)+RESET for _ in range(width)))
        time.sleep(0.02)

# ---------- Banner ----------
def banner():
    clear()
    neon=[
        f"{M}██████╗ ██████╗  ██████╗ ██╗  ██╗██╗███╗   ██╗ ██████╗ ",
        f"{C}██╔══██╗██╔══██╗██╔═══██╗██║ ██╔╝██║████╗  ██║██╔════╝",
        f"{B}██████╔╝██████╔╝██║   ██║█████╔╝ ██║██╔██╗ ██║██║  ███╗",
        f"{G}██╔═══╝ ██╔══██╗██║   ██║██╔═██╗ ██║██║╚██╗██║██║   ██║",
        f"{Y}██║     ██║  ██║╚██████╔╝██║  ██╗██║██║ ╚████║╚██████╔╝",
        f"{R}╚═╝     ╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═╝╚═╝╚═╝  ╚═══╝ ╚═════╝ {RESET}"
    ]
    for ln in neon: print(ln); time.sleep(0.02)
    print(W+"                H A C K I N G   W O R L D™"+RESET)
    print(K+"         Free Fire Diamond VIP — WORKING TOOLS"+RESET)
    print(W+"────────────────────────────────────────────────────────────\n"+RESET)

# ---------- Fake backend logs ----------
def edge_logs(user_uid, package):
    clusters=["ap-sg","in-mum","eu-fr","us-va","br-sp","jp-tyo"]
    events=[
        "Initializing kernel hooks",
        "Negotiating cipher suites",
        "Spawning ephemeral sockets",
        "Applying anti-bot fingerprints",
        "Routing shard streams",
        "Opening telemetry window"
    ]
    for ev in events:
        tag=random.choice(clusters)
        token=hex(random.getrandbits(44))
        typewrite(C+f"[{tag}] {ev}  token={token}  uid={user_uid}  pkg={package}"+RESET,0.006)
        time.sleep(0.06)

# ---------- Flow ----------
def ask_cookie():
    print(W+"Login Method: "+C+"Cookie Session (BD GAME GHOR)"+RESET)
    ck=input(Y+"[+] Paste Cookie (any text for Work): "+W).strip()
    if not ck:
        print(R+"Cookie required for the demo. Exiting."+RESET); time.sleep(1); sys.exit(0)
    spinner("[✓] Validating cookie (BD GAME GHOR)",2.0)
    return ck

def ask_uid():
    uid=input(Y+"[+] Enter Free Fire UID: "+W).strip()
    if not uid:
        print(R+"UID required. Exiting."+RESET); time.sleep(1); sys.exit(0)
    spinner("[✓] Connecting to Garena mesh (WORK)",1.8)
    print(G+f"[✓] UID Verified: {uid}"+RESET); time.sleep(0.6)
    return uid

def pick_package():
    print(W+"\nSelect Diamond Package:"+RESET)
    packs=[("Lite",500),("Boost",1000),("Pro",5000),("Ultra",10000),("Mythic",20000)]
    for i,(n,v) in enumerate(packs,1):
        print(C+f"[{i}] {n:<6} → ~{v} Diamonds"+RESET)
    choice=input(Y+"Choose (1-5): "+W).strip()
    try: idx=max(1,min(5,int(choice)))
    except: idx=3
    return packs[idx-1]

def simulate_delivery(uid, amount):
    wave_line(60,2)
    edge_logs(uid, amount)
    progress_bar("[#] Preparing shard channels",40,1.8)
    print()
    total=0; goal=amount; bar_len=42
    print(M+"[*] Injecting Diamonds (visual)…"+RESET)
    while total<goal:
        step=random.randint(max(10,goal//20), max(22,goal//12))
        total=min(goal,total+step)
        fill=int(total/goal*bar_len)
        bar=G+"█"*fill+RESET+"░"*(bar_len-fill)
        pct=int(total/goal*100)
        sys.stdout.write(C+f"Delivered: {W}{total:>6}/{goal:<6}  {bar}  {pct:3d}%\r"+RESET)
        sys.stdout.flush()
        time.sleep(random.uniform(0.04,0.09))
        if random.random()<0.07:
            sys.stdout.write("\n"+Y+"[!] Minor rate-limit encountered — smoothing traffic"+RESET+"\n")
            time.sleep(0.4)
    print("\n")
    progress_bar("[#] Verifying delivery receipts",32,1.4)
    spinner("[✓] Clearing temporary artifacts",1.6)

def finale(uid, amount):
    clear(); banner(); confetti(4,64)
    print(G+"✅ SUCCESS (WORK)"+RESET)
    print(W+f"Approximate Diamonds queued for UID {C}{uid}{W}: {G}{amount}{RESET}")
    print(K+"\nNOTE: This is a WORKING/DIAMOND only —  real diamonds are sent."+RESET)
    input(W+"\nPress Enter to exit…"+RESET)

def main():
    banner()
    # optional fast mode
    if "--fast" in sys.argv: random.seed(42)
    # Step 1: “Cookie”
    _ck=ask_cookie()
    # Step 2: UID
    uid=ask_uid()
    # Step 3: Package
    name, amount=pick_package()
    print(G+f"\n[✓] Selected Package: {name}  (~{amount} Diamonds)"+RESET)
    time.sleep(0.5)
    # Step 4: Fake “secure checks”
    spinner("[✓] Security sandbox checks",1.6)
    progress_bar("[#] Building delivery pipeline",36,1.6)
    # Step 5: Deliver (visual)
    simulate_delivery(uid, amount)
    # Step 6: Finale
    finale(uid, amount)

if __name__=="__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(RESET+"\nInterrupted.\n")