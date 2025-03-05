def NULL_not_found(object: any) -> int:
    object_type = type(object)
    if object is None:
        print("Nothing:", object, object_type)
    elif object_type is float and object != object:
        print("Cheese:", object, object_type)
    elif object_type is int and object == 0:
        print("Zero:", object, object_type)
    elif object_type is str and object == '':
        print("Empty:", object, object_type)
    elif object_type is bool and object == False:
        print("Fake:", object, object_type)
    else:
        print("Type not found")
        return 1
    return 0