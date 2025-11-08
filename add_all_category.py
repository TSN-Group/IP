# add_all_category.py

# Input and output file names
input_file = "channels.m3u"
output_file = "channels_with_all.m3u"

# Read original M3U
with open(input_file, "r", encoding="utf-8") as f:
    lines = f.readlines()

# Prepare containers
all_category = ["#EXTM3U\n"]
channels = []

# Collect all #EXTINF and their next line (URL)
for i in range(len(lines)):
    if lines[i].startswith("#EXTINF"):
        if i + 1 < len(lines):
            extinf = lines[i]
            url = lines[i + 1]

            # Duplicate channel, replace group-title with "ALL"
            new_extinf = extinf
            if "group-title=" in new_extinf:
                # Replace the group-title content only
                import re
                new_extinf = re.sub(r'group-title="[^"]+"', 'group-title="ALL"', new_extinf)
            else:
                # If no group-title exists, add it
                new_extinf = new_extinf.replace("#EXTINF:-1", '#EXTINF:-1 group-title="ALL"')

            all_category.append(new_extinf)
            all_category.append(url)
            channels.append(extinf)
            channels.append(url)

# Write final M3U: ALL category first + original list
with open(output_file, "w", encoding="utf-8") as f:
    f.writelines(all_category)
    f.write("\n# -----------------------\n# Original Categories\n# -----------------------\n")
    f.writelines(channels)

print(f"✅ Done! Saved as {output_file}")
