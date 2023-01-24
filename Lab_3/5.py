def update_records(rec_dict,id,property,value):
    if property != 'tracks' and value != '':
        rec_dict[id][property] = value
    elif property == 'tracks' and rec_dict[id]['track'] == None:
        rec_dict[id]['tracks'] = value
    elif property == 'tracks' and value != '':
        rec_dict[id]['tracks'] += value
    elif value == '':
        rec_dict[id].pop(property)
