class Solution:
    def trap(self, heights: List[int]) -> int:
        return self.trap_v2(heights)

    def trap_v2(self, heights: List[int]) -> int:
        self.heights = heights
        self.water = 0
        self.dead_indices = set()

        while True:
            # sorted heights 
            sorted_heights = self.sort_them(self.heights)

            what = self.next_non_dead(sorted_heights)
            if not what:
                break
            i, h = what
            
            # if we updated the height, skip,
            #if h != self.heights[i]:
            #    continue

            found_concavity = self.explore(i, h + 1)
                
        return self.water

    def sort_them(self, heights):
        return sorted(
            [[i, h] for (i, h) in enumerate(heights)],
            key=lambda x: x[1]
        )

    def next_non_dead(self, sorted_heights):
        non_dead_heights = [
            [i, h] for (i, h) in sorted_heights
            if i not in self.dead_indices
        ]
        if non_dead_heights:
            return non_dead_heights[0]

    def explore(self, i, h):
        left_hit, left_set = self.edge_exists2(i, h, "left")
        right_hit, right_set = self.edge_exists2(i, h, "right")

        if left_hit and right_hit:
            for position in left_set | right_set:
                # raise those heights
                self.heights[position] += 1

                self.water += 1
            return True
        
        # add them to the dead indices 
        self.dead_indices |= left_set | right_set
        return False

    def edge_exists2(self, i, j, direction):
        memory = set([i])
        if direction == "left":
            i -= 1
            # look left until we see an edge 
            while i >= 0:
                
                if self.heights[i] >= j:
                    return True, memory
                memory.add(i)
                i -= 1
        else:
            i += 1
            # look right until an edge
            while i < len(self.heights):
                
                if self.heights[i] >= j:
                    return True, memory
                memory.add(i)
                i += 1
        return False, memory


    def trap_v1(self, heights: List[int]) -> int:
        roof = max(heights)
        self.heights = heights
        water = 0
        # brute force, for every x value, check for left and right convexity.
        # If we have it, then water += 1. 
        # Check for every (x,y) until the max height.

        for i in range(1, len(heights) - 1):  # skip first and last, since they have no support by definition.
            h = heights[i]
            for j in range(h + 1, roof + 1):
                # look left and right
                if (self.edge_exists(i, j, "left") 
                    and self.edge_exists(i, j, "right")
                ):
                    water +=1 
        return water      

    def edge_exists(self, i, j, direction):
        
        if direction == "left":
            i -= 1
            # look left until we see an edge 
            while i >= 0:
                if self.heights[i] >= j:
                    return True
                i -= 1
        else:
            i += 1
            # look right until an edge
            while i < len(self.heights):
                if self.heights[i] >= j:
                    return True
                i += 1
        return False

        