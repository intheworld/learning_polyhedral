import isl
import pet


if __name__ == '__main__':
    scop = pet.scop.extract_from_C_source("demo/matmul.c".encode("utf-8"), "matmul".encode("utf-8"))

    schedule = scop.get_schedule()
    print(scop.get_context())
    print("\n")
    node = schedule.get_root().child(0)
    node = node.member_set_coincident(0, True)
    node = node.child(0)
    node = node.member_set_coincident(0, True)
    print(node)