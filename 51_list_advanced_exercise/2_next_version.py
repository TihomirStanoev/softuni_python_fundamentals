old_version = input().split('.')

old_version_string = ''.join(old_version)
new_version = int(old_version_string) + 1

print('.'.join(str(new_version)))