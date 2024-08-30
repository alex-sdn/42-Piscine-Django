from django.shortcuts import render

def get_shades(r, g, b):
    shades = []
    for i in range(50):
        shades.append(f'rgb({int(r * (i / 49))},{int(g * (i / 49))},{int(b * (i / 49))})')
    return shades

def table(request):
    black_shades =  get_shades(255, 255, 255)
    red_shades =    get_shades(255, 0, 0)
    blue_shades =   get_shades(0, 0, 255)
    green_shades =  get_shades(0, 255, 0)

    rows = zip(black_shades, red_shades, blue_shades, green_shades)

    context = {'rows': rows}
    return render(request, 'ex03/table.html', context)
