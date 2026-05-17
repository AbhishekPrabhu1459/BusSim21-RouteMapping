def overlap_penalty(routes):

    penalty = 0

    for i in range(len(routes)):

        for j in range(i + 1, len(routes)):

            overlap = set(routes[i].stops).intersection(
                routes[j].stops
            )

            # Small overlap is okay for transfers
            # Large overlap is bad

            if len(overlap) > 2:

                penalty += (
                    len(overlap) * 100
                )

    return penalty