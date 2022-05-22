import isl
import pet


if __name__ == '__main__':
    pet.options.set_autodetect(True)
    scop = pet.scop.extract_from_C_source(b'demo/false.c', b'f')
    schedule = scop.get_schedule()
    may_read = scop.get_may_reads()
    may_write = scop.get_may_writes()
    must_write = scop.get_must_writes()

    access = isl.union_access_info(may_read)
    access = access.set_may_source(may_write)
    access = access.set_must_source(must_write)
    access = access.set_schedule(schedule)
    flow = access.compute_flow()
    print("May-flow dependences:")
    print(flow.get_may_dependence())
    print("May-live-in accesses:")
    print(flow.get_may_no_source())

