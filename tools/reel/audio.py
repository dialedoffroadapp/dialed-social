import numpy as np, wave, json, sys
cfg=json.load(open(sys.argv[1])); out=sys.argv[2]
sr=44100; dur=13.4; n=int(sr*dur); a=np.zeros(n); t=np.arange(n)/sr
pad=(np.sin(2*np.pi*55*t)*0.5+np.sin(2*np.pi*82.4*t)*0.3+np.sin(2*np.pi*110*t)*0.15)
env=np.clip(t/1.5,0,1)*np.clip((dur-t)/1.2,0,1)*(0.75+0.25*np.sin(2*np.pi*t*2.0))
a+=pad*env*0.18
rng=np.random.default_rng(1)
def click(at,amp=0.6,f=2400):
    i=int(at*sr); L=int(0.03*sr); k=np.arange(L)/sr
    a[i:i+L]+=amp*np.sin(2*np.pi*f*k)*np.exp(-k*180)+amp*0.5*rng.uniform(-1,1,L)*np.exp(-k*300)
def thump(at,amp=0.7):
    i=int(at*sr); L=int(0.25*sr); k=np.arange(L)/sr
    a[i:i+L]+=amp*np.sin(2*np.pi*(60+80*np.exp(-k*30))*k)*np.exp(-k*14)
thump(0.1,0.6); thump(0.7,0.6)
for i in range(5): thump(2.6+i*0.95,0.35)
flips=[2.6+i*0.95+0.45 for i,r in enumerate(cfg['rows']) if r[3]]
for at,c in zip(flips,cfg['ticks']):
    for j in range(min(c,4)): click(at+j*0.08)
thump(7.85,0.7); thump(10.15,0.7)
a=a/np.max(np.abs(a))*0.8
w=wave.open(out,'wb'); w.setnchannels(1); w.setsampwidth(2); w.setframerate(sr); w.writeframes((a*32767).astype(np.int16).tobytes()); w.close()
