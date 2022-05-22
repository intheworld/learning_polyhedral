import isl
import pet

if __name__ == '__main__':
    pet.options.set_autodetect(True)
    scop = pet.scop.extract_from_C_source(b"demo/false.c", b"f")
    schedule = scop.get_schedule()
    may_read = scop.get_tagged_may_reads()
    may_write = scop.get_tagged_may_writes()
    must_write = scop.get_tagged_must_writes()
    tagged_instances = may_write.union(may_read).domain()
    tagged_instances = tagged_instances.unwrap()
    drop_tags = tagged_instances.domain_map_union_pw_multi_aff()
    schedule = schedule.pullback(drop_tags)

    access = isl.union_access_info(may_read)
    access = access.set_may_source(may_write)
    access = access.set_must_source(must_write)
    access = access.set_schedule(schedule)
    flow = access.compute_flow()
    print("Tagged may-read access relation:")
    print(may_read)
    print("Tagged may-write access relation:")
    print(may_write)
    print("Tagged may-flow dependences:")
    print(flow.get_may_dependence())
    print("Tagged may-live-in accesses:")
    print(flow.get_may_no_source())
