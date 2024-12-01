namespace AoC.Library.Helpers;

public static class PathUtils
{
    /// <returns>Base directory of the project instead of the bin folder</returns>
    public static string GetBaseDirectory() => Directory.GetParent(AppContext.BaseDirectory)!.Parent!.Parent!.Parent!.FullName;
}