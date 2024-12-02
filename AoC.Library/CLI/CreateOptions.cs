using CommandLine;

namespace AoC.Library.CLI
{
    [Verb("create", HelpText = "Create a folder for the current or specified day.")]
    public class CreateOptions
    {
        [Option('d', "day", HelpText = "Day to create. Defaults to today's day.")]
        public int? Day { get; set; }
    }
}
