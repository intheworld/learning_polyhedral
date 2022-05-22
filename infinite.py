import pet

if __name__ == '__main__':
    pet.options.set_autodetect(True)
    scop = pet.scop.extract_from_C_source("demo/infinite.c".encode("utf-8"), "f".encode("utf-8"))
    print(scop.get_must_writes())
    schedule = scop.get_schedule()
    node = schedule.get_root().child(0).child(1).child(0)
    print(node)
