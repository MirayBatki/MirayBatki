from xml.dom import minidom

def format_plural(unit):
    """
    Returns a properly formatted number
    """
    return 's' if unit != 1 else ''


def svg_overwrite(filename, age_data):
    """
    Parse SVG files and update elements with static data
    """
    svg = minidom.parse(filename)
    f = open(filename, mode='w', encoding='utf-8')
    tspan = svg.getElementsByTagName('tspan')
    tspan[30].firstChild.data = age_data
    # You can customize the text fields here for other static information
    f.write(svg.toxml('utf-8').decode('utf-8'))
    f.close()


if __name__ == '__main__':

    # SVG generation (for both dark and light mode)
    svg_overwrite('dark_mode.svg', age_data)
    svg_overwrite('light_mode.svg', age_data)
