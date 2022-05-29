import isl
import pet

def test_compute_schedule():
    pet.options.set_autodetect(True)
    scop = pet.scop.extract_from_C_source(b'demo/matmul.c', b'matmul')
    schedule = scop.get_schedule()
    may_read = scop.get_may_reads()
    may_write = scop.get_may_writes()
    must_write = scop.get_must_writes()

    access = isl.union_access_info(may_read)
    access = access.set_may_source(may_write)
    access = access.set_must_source(must_write)
    access = access.set_schedule(schedule)
    flow = access.compute_flow()
    dependency = flow.get_full_may_dependence()
    print("May-flow dependences:")
    print(dependency)

    dm = schedule.domain()
    print("domain:")
    print(dm)
    cst = isl.schedule_constraints.on_domain(dm)
    cst = cst.set_validity(dependency)
    sub_schedule = isl.schedule_constraints.compute_schedule(cst)

    print("origin schedule:")
    print(schedule.get_root().child(0))

    print("new schedule:")
    print(sub_schedule.get_root().child(0))
    # 结果看起来有问题，constraint应该不够



if __name__ == '__main__':
    context = isl.set("{ : }")
    domain = isl.set("{S[t,i] : 1 <=t<= 5 and 1 <=i<=10}")

    schedule = isl.map("{ S[t,i] -> T[t+1, i+t+10] }")

    schedule_domain = schedule.intersect_domain(domain)

    build = isl.ast_build.from_context(context)
    ast = build.node_from_schedule_map(schedule_domain)
    print(ast.to_C_str())

    print("\n")
    test_compute_schedule()

