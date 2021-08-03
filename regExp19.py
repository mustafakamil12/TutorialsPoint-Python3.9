import re

address = "#TZ=godric#"

default_match = re.match('#TZ=(\w*)#',address)

print(f"default_match = {default_match}")
print(f"default_match = {default_match.group(0)}")
print(f"default_match = {default_match.group(1)}")


if (default_match):
    offset = GFS_timezone.get_timezone_offset([current_time,default_match.group(1)])
    print(f"offset = {offset}")
    address = re.sub('#TZ=(\w*)#',"", address)
final_address = current_time.as_text(address,offset)
print(f"final_address = {final_address}")
