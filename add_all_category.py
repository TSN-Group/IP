def add_all_channels_category(input_file, output_file, new_category='All Channels'):
    # Open and read the input M3U file
    with open(input_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    # Initialize a list to hold the modified lines
    modified_lines = []

    # Add new category (All Channels) at the beginning
    modified_lines.append('#EXTINF:-1, group-title="{}"\n'.format(new_category))

    # Iterate through all lines in the original M3U file
    for line in lines:
        if line.startswith('#EXTINF:'):
            # Add the original channel details under the new "All Channels" category
            modified_lines.append(line)
        else:
            # Keep all other lines (URLs, etc.)
            modified_lines.append(line)

    # Write the modified lines to the output file
    with open(output_file, 'w', encoding='utf-8') as f:
        f.writelines(modified_lines)

    print(f"Updated playlist with 'All Channels' category saved to {output_file}")


# Example usage
input_file = 'input_playlist.m3u'  # Input M3U playlist file
output_file = 'output_playlist.m3u'  # Output M3U playlist file
add_all_channels_category(input_file, output_file)
