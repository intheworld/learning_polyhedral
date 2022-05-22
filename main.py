import pet

if __name__ == '__main__':
    # s = isl.union_set("{B[6]; A[2,8,1]; B[5]}")
    # print(s)
    pet.options.set_autodetect(True)
    scop = pet.scop.extract_from_C_source("demo/inner.c".encode("utf-8"), "inner".encode("utf-8"))
    print(scop.get_must_writes())
    schedule = scop.get_schedule()
    node = schedule.get_root().child(0).child(1).child(0)
    print(node)

