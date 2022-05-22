import isl
import pet

if __name__ == "__main__":
    scop = pet.scop.extract_from_C_source(b"demo/live-out.c", b"g")
    schedule = scop.get_schedule()
    may_write = scop.get_may_writes()
    must_write = scop.get_must_writes()
    kill = scop.get_must_kills()

    access = isl.union_access_info(must_write.union(kill))
    access = access.set_may_source(may_write)
    access = access.set_schedule(schedule)
    flow = access.compute_flow()
    dep = flow.get_full_may_dependence()
    killed = dep.range_factor_range()
    live_out = may_write.subtract(killed)
    print(live_out)
