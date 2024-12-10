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


        public void AddEdge(Vertex<T> source, Vertex<T> destination)
        {
            ArgumentNullException.ThrowIfNull(source);
            ArgumentNullException.ThrowIfNull(destination);

            _adjacencyList.TryAdd(source, []);
            _adjacencyList[source].Add(destination);
        }

        public IEnumerable<List<Vertex<T>>> GetPaths(Vertex<T> source, Vertex<T> destination)
        {
            ArgumentNullException.ThrowIfNull(source);
            ArgumentNullException.ThrowIfNull(destination);

            return GetPathsRecursive(source, destination, []);
        }

        private IEnumerable<List<Vertex<T>>> GetPathsRecursive(
            Vertex<T> current,
            Vertex<T> destination,
            HashSet<Vertex<T>> visited,
            List<Vertex<T>>? currentPath = null)
        {
            currentPath ??= [current];

            if (current.Equals(destination))
            {
                yield return new List<Vertex<T>>(currentPath);
                yield break;
            }

            var pathVisited = new HashSet<Vertex<T>>(visited) { current };

            if (!_adjacencyList.TryGetValue(current, out var neighbors))
            {
                yield break;
            }

            foreach (var neighbor in neighbors)
            {
                if (pathVisited.Contains(neighbor))
                {
                    continue;
                }

                var newPath = new List<Vertex<T>>(currentPath) { neighbor };

                foreach (var path in GetPathsRecursive(neighbor, destination, pathVisited, newPath))
                {
                    yield return path;
                }
            }
        }

        public bool HasPath(Vertex<T> source, Vertex<T> destination)
        {
            ArgumentNullException.ThrowIfNull(source);
            ArgumentNullException.ThrowIfNull(destination);

            return GetPaths(source, destination).Any();
        }
    }
}
