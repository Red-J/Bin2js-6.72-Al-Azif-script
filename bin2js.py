import sys
 
output = ""
 
with open(sys.argv[1], 'rb') as buf:
    payload = ["0x{:02x}".format(b) for b in buf.read()]
 
size = len(payload)
 
output += "var payload = ["
 
count = 0
for x in payload:
  count = count + 1
  output += "{}".format(int(x, 16))
  if count < size:
    output += ","
 
output += "];\n\n"
 
output += "window.mira_blob_2_len = {};\n".format(hex(size))
output += "window.mira_blob_2 = malloc(window.mira_blob_2_len);\n"
output += "write_mem(window.mira_blob_2, payload);\n"
 
if len(sys.argv) > 2:
  output_file = sys.argv[2]
else:
  output_file = "payload.js"
 
with open(output_file, "w") as buf:
  buf.write(output)

//python3 .py .bin
