#!/bin/bash
# Print Apple Calendar events for the next N days (default 7), one per line, sorted:
#   YYYY-MM-DD HH:MM-HH:MM | title | calendar
# Skips holiday, birthday and suggestion calendars. Needs Calendar access for the terminal (macOS prompts once).
days="${1:-7}"
osascript - "$days" <<'OSA' | sort
on pad(n)
	return text -2 thru -1 of ("0" & n)
end pad
on fmt(d)
	return (year of d as text) & "-" & my pad(month of d as integer) & "-" & my pad(day of d) & " " & my pad(hours of d) & ":" & my pad(minutes of d)
end fmt
on run argv
	set startD to current date
	set time of startD to 0
	set endD to startD + ((item 1 of argv) as integer) * days
	set out to {}
	tell application "Calendar"
		repeat with c in calendars
			set cn to name of c
			if cn does not contain "Holiday" and cn does not contain "Birthday" and cn does not contain "Siri" then
				repeat with e in (every event of c whose start date >= startD and start date < endD)
					set s to start date of e
					set f to end date of e
					set end of out to my fmt(s) & "-" & my pad(hours of f) & ":" & my pad(minutes of f) & " | " & (summary of e) & " | " & cn
				end repeat
			end if
		end repeat
	end tell
	set AppleScript's text item delimiters to linefeed
	return out as text
end run
OSA
