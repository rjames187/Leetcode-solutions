function hasCycle(graph: Map<number, number[]>, inDegrees: Map<number, number>): boolean {
    const q = []
    for (const course of inDegrees.keys()) {
        if (inDegrees.get(course) === 0) q.push(course)
    }
    while (q.length) {
        const course = q.shift()
        for (const recipient of graph.get(course)) {
            inDegrees.set(recipient, inDegrees.get(recipient) - 1)
            if (inDegrees.get(recipient) === 0) q.push(recipient)
        }
        graph.delete(course)
    }
    if (graph.size) return false
    return true
}

function canFinish(numCourses: number, prerequisites: number[][]): boolean {
    const graph = new Map()
    const inDegrees = new Map()
    for (let i = 0; i < numCourses; i++) {
        inDegrees.set(i, 0)
        graph.set(i, [])
    }
    for (const req of prerequisites) {
        graph.get(req[1]).push(req[0])
        inDegrees.set(req[0], inDegrees.get(req[0]) + 1)
    }
    return hasCycle(graph, inDegrees)
}