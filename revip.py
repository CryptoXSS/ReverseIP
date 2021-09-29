import requests, sys, subprocess, blessed

# Made by z3ntl3
# RGB Would only work on 256 colored terminals
# How to get 256 Color on me terminal?: just type: export TERM=xterm-256color
term = blessed.Terminal()
d1 = term.color_rgb(200, 20, 245)

reset = term.reset()
underline = term.underline()
def run():
    
    try:
        print(f'{d1}')
        print(r'''
              (
               )
              (
        /\  .-"""-.  /\
       //\\/  ,,,  \//\\
       |/\| ,;;;;;, |/\|
       //\\\;-"""-;///\\
      //  \/   .   \/  \\
     (| ,-_| \ | / |_-, |)
       //`__\.-.-./__`\\
      // /.-(() ())-.\ \\
     (\ |)   '---'   (| /)
      ` (|           |) `
        \)           (/
''')
        d2 = term.color_rgb(207, 68, 242)
        d3 = term.color_rgb(215, 84, 247)
        d4 = term.color_rgb(220, 100, 250)
        d5 = term.color_rgb(227, 124, 252)
        d6 = term.color_rgb(230, 139, 252)
        d7 = term.color_rgb(231, 155, 250)
        d8 = term.color_rgb(240, 181, 255)
        print(f'{reset}{underline}{d2}Rev{d3}ers{d4}e {d5}I{d6}P {d7}Loo{d8}kup{reset}\n\033[31m───\033[32m﹥ made by z3ntl3 - t.me/z3ntl3')

        url = sys.argv[1]
        
        
       

        api = requests.get(f"https://api.hackertarget.com/reverseiplookup/?q={url}", headers={'Cache-Control': 'no-cache'}) 
        # if you have a premium api replace the string with: f"https://api.hackertarget.com/reverseiplookup/?q={url}&page=2&apikey=zzzzzzz"
        raw = api.text
        

        subprocess.run('sudo rm -r data.txt', shell=True)
        with open('data.txt', '+a')as f:
            f.write(raw)
            f.close()
        b = term.color_rgb(255, 105, 197)
        print(f'\n{b}[{d2}C{d3}omp{d4}le{d5}ted{d8}!{b}]:\n\033[31m───\033[32m﹥ {d8}Sav{d7}e{d6}d {d5}i{d4}n {d3}dat{d2}a.{d1}txt')
        sys.exit()
        
    except:
        print('\033[31m───\033[32m﹥ \033[0mUsage: python3 revip.py url\n')

if __name__ == "__main__":
    run()
