# -*- coding: unicode -*-

def display_map(data_map, data_ui):
    # Check which player have to play and define displaying constants.
    ui_color = Fore.BLUE
    player = 'player1'

    data_cell = {'ui_color': ui_color}

    # Generate the units to be displayed.
    for i in range(1, data_map['map_size'] + 1):
        for j in range(1, data_map['map_size'] + 1):

            # Coloration black/white of the cells.
            background_cell = ''
            if (i + j) % 2 == 0:
                background_cell = Back.WHITE

            if (i, j) in data_map['player1']:
                data_cell['(' + str(i) + ',' + str(j) + ')'] = data_map['player1'][(i, j)][1] + background_cell + ' ☻' + str(data_map['player1'][(i, j)][0]) + (str(data_map['player1'][(i, j)][2]) + ' ')[:2]
            elif (i, j) in data_map['player2']:
                data_cell['(' + str(i) + ',' + str(j) + ')'] = data_map['player2'][(i, j)][1] + background_cell + ' ☻' + str(data_map['player2'][(i, j)][0]) + (str(data_map['player2'][(i, j)][2]) + ' ')[:2]
            else:
                data_cell['(' + str(i) + ',' + str(j) + ')'] = background_cell + (' ' * 5)

    # Generate the statistics to be displayed.

    # Generate the title of the map to be displayed.
    data_cell['turn'] = str(data_map['main_turn']/2 + 1)
    data_cell['playername'] = 'Michel'
    data_cell['blank'] = (81 - len(data_cell['turn']) - len(data_cell['playername'])) * ' '

    # Print the top of the UI.
    for line in data_ui[:3]:
        print line % data_cell

    # Print the top of the grid.
    print data_ui[3] % data_cell
    print data_ui[4] % data_cell

    # Print the map.
    for line in data_ui[6: data_map['map_size'] + 6]:
        print line % data_cell

    # Print the foot of the grid.
    for line in data_ui[data_map['map_size'] + 5, data_map['map_size'] + 8]:
        print line % data_cell
