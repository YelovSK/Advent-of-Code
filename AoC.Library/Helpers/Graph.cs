namespace AoC.Library.Helpers
{
    public class Vertex<T>
    {
        public readonly T Value;
        private readonly int _hashCode;

        /// <summary>
        /// HashCode based on <see cref="Value"/>
        /// </summary>
        public Vertex(T value)
        {
            ArgumentNullException.ThrowIfNull(value);

            _hashCode = value.GetHashCode();
            Value = value;
        }

        public Vertex(T value, int hashCode)
        {
            ArgumentNullException.ThrowIfNull(value);

            _hashCode = hashCode;
            Value = value;
        }

        public override bool Equals(object obj)
        {
            return obj is Vertex<T> vertex && GetHashCode() == vertex.GetHashCode();
        }

        public override int GetHashCode()
        {
            return _hashCode;
        }

        public override string ToString()
        {
            return Value.ToString();
        }
    }

    public class Graph<T>
    {
        private readonly Dictionary<Vertex<T>, HashSet<Vertex<T>>> _adjacencyList;

        public Graph()
        {
            _adjacencyList = [];
        }

        public List<Vertex<T>> GetAllVertices()
        {
            var keys = _adjacencyList.Keys.ToHashSet();
            var values = _adjacencyList.Values.SelectMany(_ => _).ToHashSet();
            return keys.Union(values).ToList();
        }


        public void AddEdge(Vertex<T> start, Vertex<T> end)
        {
            ArgumentNullException.ThrowIfNull(start);
            ArgumentNullException.ThrowIfNull(end);

            _adjacencyList.TryAdd(start, []);
            _adjacencyList[start].Add(end);
        }

        public IEnumerable<List<Vertex<T>>> GetPaths(Vertex<T> start, Vertex<T> end)
        {
            var stack = new Stack<(Vertex<T> Current, List<Vertex<T>> Path)>();
            stack.Push((start, new List<Vertex<T>> { start }));

            while (stack.Count > 0)
            {
                var (current, path) = stack.Pop();

                if (current.Equals(end))
                {
                    yield return path;
                    continue;
                }

                if (!_adjacencyList.TryGetValue(current, out var neighbours))
                {
                    continue;
                }

                foreach (var neighbour in neighbours.Where(n => !path.Contains(n)))
                {
                    if (!path.Contains(neighbour)) // Avoid cycles
                    {
                        var newPath = new List<Vertex<T>>(path) { neighbour };
                        stack.Push((neighbour, newPath));
                    }
                }
            }
        }
        public bool HasPath(Vertex<T> start, Vertex<T> end)
        {
            ArgumentNullException.ThrowIfNull(start);
            ArgumentNullException.ThrowIfNull(end);

            return GetPaths(start, end).Any();
        }
    }
}
