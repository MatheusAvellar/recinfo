import random, json

N = 1000

with open("./within-wikipedia-tr-01.jsonl", encoding="utf8") as in_matches:
  with open("./out.txt", "a", encoding="utf8") as out_matches:
    while N > 0:
      line = next(in_matches)
      if random.randint(0,1000) > 998:
        match = json.loads(line)
        txt = match[2]
        if ("village" in txt
          or "town" in txt
          or "city" in txt
          or "census" in txt or "Census" in txt
          or "district" in txt
          or "municipality" in txt
          or "enzyme" in txt
          or "species" in txt):
          continue
        start = match[2][:25]
        end = match[2][-25:]
        match[2] = [ start, end ]

        start = match[3][:25]
        end = match[3][-25:]
        match[3] = [ start, end ]

        out_matches.write(f"{json.dumps(match)}\n")
        N = N - 1
        if N % 10 == 0:
          print(N)

print("N is done!")
