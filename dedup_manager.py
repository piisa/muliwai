#deduplicate text data at the sentence level. 
import glob, os, tqdm
from torch import multiprocessing

strip_chars = " ,،、{}[]|()\"'“”《》«»!:;?.。…．"                  
def dedup_document(lines, dup_hash, simhash_index=None, src_lang="en", min_line_len=150, sim_hash_threshold=0.9):
  if type(lines) is str:
    lines = [lines]
  ret = []
  i = 0
  for line in lines:
    line = line.decode().strip()
    if len(line) < min_line_len: 
        #print ('skipping', line)
        continue
    all_lines = []
    line = line.replace("。", ". ").replace(".\"", "\".").replace(".”", "”.").replace(".》", "》.").replace(".»", "».")
    for line2 in line.split(". "):
        line3 = line2.lower().replace(" ", "").strip()
        if not line3: continue
        code = hash(line3)
        if code in dup_hash:
              if len(line3) < 15:
                #print ('found dup but short line', line2)
                all_lines.append(line2+".")
                continue
              #print ('dup', line2)
        else:
              dup_hash[code] = 1
              all_lines.append(line2 +".")
    if all_lines: 
        line4 = " ".join(all_lines)
        if line4[-2] in strip_chars:
              line4 = line4[:-1]
        if len(line4) < min_line_len: continue
            ret.append(line4)
        i+=1
        if i+1%1000==0:
          pass
          #print out status
  return ret
