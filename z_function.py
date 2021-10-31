# z функция за O(n)
def z_function(pattern, text):
    s = pattern + '&' + text
    mass_z = [0 for i in range(len(s))]
    t, r = 0, 0
    for i in range(1, len(s)):
        if r > i:
            mass_z[i] = min(mass_z[i - t], r - i + 1)
        else:
            mass_z[i] = 0
        while i + mass_z[i] < len(s) and s[mass_z[i]] == s[mass_z[i] + i]:
            mass_z[i] += 1
        if i + mass_z[i] > r:
            r = i + mass_z[i]
            t = i
    return mass_z

# z функция за O(n^2)
def z_function_n(pattern, text):
    s = pattern + '&' + text
    mass_z = [0 for i in range(len(s))]
    for i in range(1, len(s)):
        while i + mass_z[i] < len(s) and s[mass_z[i]] == s[mass_z[i] + i]:
            mass_z[i] += 1
    return mass_z


pattern = input()
text = input()

z_func, count = z_function(pattern, text)

z_func_n, count_n = z_function_n(pattern, text)

print(z_func, count, len(pattern+text))
print(z_func_n, count_n, len(pattern+text))

