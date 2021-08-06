import re

#post_proc = None
post_proc = "#TZ=godric#"

if post_proc != None and len(post_proc) > 0:
    offset = 0

    default_match = re.match('#TZ=(\w*)#',post_proc)
    if (default_match):
        #offset = GFS_timezone.get_timezone_offset([current_time.get_time_t(),default_match.group(1)])
        post_proc = re.sub('#TZ=(\w*)#',"",post_proc)
    #final_post_proc = current_time.as_text(post_proc,offset)

#final_post_proc = re.sub('\$','\\\$',final_post_proc)
#final_post_proc = re.sub(' (\S*[\$#]\S*) ',f"\'\"\'\"\'\"{final_post_proc}\"\'\"\'\"\'" ,final_post_proc)
