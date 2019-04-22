def solution(bridge_length, weight, truck_weights):

    time = 0
    weights_on_bridge = 0
    # truck_locations = [0 for i in range(len(truck_weights))]
    truck_loc_on_the_bridge = []
    truck_weight_on_the_bridge = []

    while truck_weights:
        time += 1

        # 모든 다리위의 트럭의 위치를 +1 씩 증가시킨다.
        truck_loc_on_the_bridge = list(map(lambda i: i+1, truck_loc_on_the_bridge))

        # 만약 가장 선두의 트럭의 위치가 다리길이가 되면 브리지에서 내리고, 무게도 빼준다
        if truck_loc_on_the_bridge and (truck_loc_on_the_bridge[0] > bridge_length):
            weights_on_bridge -= truck_weight_on_the_bridge.pop(0)
            truck_loc_on_the_bridge.pop(0)

        # 한 대 더 들어갈 여력이 있으면
        if (weights_on_bridge + truck_weights[0]) <= weight:
            truck = truck_weights.pop(0)
            # 1. 브리지 위에 무게 더해 줌
            weights_on_bridge += truck

            # 1.1 해당 트럭의 무게를 리스트에 기록해둔다
            truck_weight_on_the_bridge.append(truck)

            # 2. 해당 트럭을 브리지위에 올린다
            truck_loc_on_the_bridge.append(1)


    answer = time + bridge_length

    return answer


if __name__ == '__main__':
    bridge_length = 2
    weight = 10
    truck_weights = [7, 4, 5, 6]

    print(solution(bridge_length, weight, truck_weights))
