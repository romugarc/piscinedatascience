def all_thing_is_obj(object: any) -> int:
    object_type = type(object)
    if object_type is list:
        print("List : ", object_type)
    elif object_type is tuple:
        print("Tuple : ", object_type)
    elif object_type is set:
        print("Set : ", object_type)
    elif object_type is dict:
        print("Dict : ", object_type)
    elif object_type is str:
        print(object, "is in the kitchen :", object_type)
    else:
        print("Type not found")
    return 42