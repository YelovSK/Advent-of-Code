namespace AoC.Library.Helpers
{
    public static class GridHelper
    {
        public static bool IsInBounds(Position position, Size size) => (position.X >= 0 && position.X < size.Height && position.Y >= 0 && position.Y < size.Width);
    }

    public struct Position : IEquatable<Position>
    {
        public int X { get; set; }
        public int Y { get; set; }

        public Position(int x, int y)
        {
            X = x;
            Y = y;
        }

        public bool Equals(Position other)
        {
            return other.X == X && other.Y == Y;
        }

        public override bool Equals(object obj)
        {
            return obj is Position position && Equals(position);
        }

        public override int GetHashCode()
        {
            return HashCode.Combine(X, Y);
        }
    }

    public struct Size : IEquatable<Size>
    {
        public int Width { get; set; }
        public int Height { get; set; }

        public Size(int width, int height)
        {
            Width = width;
            Height = height;
        }

        public bool Equals(Size other)
        {
            return other.Width == Width && other.Height == Height;
        }

        public override bool Equals(object obj)
        {
            return obj is Size size && Equals(size);
        }

        public override int GetHashCode()
        {
            return HashCode.Combine(Width, Height);
        }

        public override string ToString() => $"{Width} {Height}";
    }
}
