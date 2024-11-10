import csv

absentee_requirements = [
    {
        "State": "Alabama",
        "Excuse Required": "Yes",
        "Application Deadline": "Received by 5 PM, 5 days before Election Day",
        "Submission Methods": "Mail, In-Person",
        "Acceptable Excuses": [
            "Being out of the county on Election Day",
            "Physical illness or infirmity",
            "Working a required shift of 10 hours or more that coincides with polling hours",
            "Being enrolled as a student outside the county",
            "Being a member of the armed forces or a spouse/dependent of such a person",
            "Being appointed as an election officer or poll watcher outside your precinct",
            "Being incarcerated but otherwise eligible to vote"
        ],
        "ID or Other Requirements": "Copy of valid photo ID must be submitted with absentee ballot application."
    },
    {
        "State": "Alaska",
        "Excuse Required": "No",
        "Application Deadline": "Received 10 days before Election Day",
        "Submission Methods": "Mail, Online, In-Person",
        "Acceptable Excuses": "Not applicable; no excuse required.",
        "ID or Other Requirements": "Voter's signature on the absentee ballot must be witnessed by an authorized official or attested by one witness aged 18 or older."
    },
    {
        "State": "Arizona",
        "Excuse Required": "No",
        "Application Deadline": "Received by 5 PM, 11 days before Election Day",
        "Submission Methods": "Mail, Online, In-Person",
        "Acceptable Excuses": "Not applicable; no excuse required.",
        "ID or Other Requirements": "No ID required to request an absentee ballot; however, the voter's signature on the ballot affidavit is verified against the signature on file."
    },
    {
        "State": "Arkansas",
        "Excuse Required": "Yes",
        "Application Deadline": "Received 7 days before Election Day",
        "Submission Methods": "Mail, In-Person",
        "Acceptable Excuses": [
            "Being unavoidably absent from your polling site on Election Day",
            "Illness or physical disability",
            "Being a member of the armed forces or merchant marine, a spouse or dependent family member",
            "Being a U.S. citizen domiciled in Arkansas but temporarily living outside the territorial limits of the United States"
        ],
        "ID or Other Requirements": "Copy of valid photo ID must be submitted with absentee ballot application."
    },
    {
        "State": "California",
        "Excuse Required": "No",
        "Application Deadline": "Received 7 days before Election Day",
        "Submission Methods": "Mail, Online, In-Person",
        "Acceptable Excuses": "Not applicable; no excuse required.",
        "ID or Other Requirements": "No ID required to request or submit an absentee ballot."
    },
    {
        "State": "Colorado",
        "Excuse Required": "No",
        "Application Deadline": "Received by 8 PM on Election Day",
        "Submission Methods": "Mail, In-Person",
        "Acceptable Excuses": "Not applicable; no excuse required.",
        "ID or Other Requirements": "No ID required to request an absentee ballot; however, first-time voters may need to provide a copy of ID with their ballot."
    },
    {
        "State": "Connecticut",
        "Excuse Required": "Yes",
        "Application Deadline": "Received by Election Day",
        "Submission Methods": "Mail, In-Person",
        "Acceptable Excuses": [
            "Active service in the Armed Forces",
            "Absence from town during all election hours",
            "Illness",
            "Physical disability",
            "Religious tenets forbidding secular activity on Election Day",
            "Serving as an election official at a polling place other than your own",
            "Physical disability"
        ],
        "ID or Other Requirements": "No ID required to request an absentee ballot."
    },
    {
        "State": "Delaware",
        "Excuse Required": "Yes",
        "Application Deadline": "Received 4 days before Election Day",
        "Submission Methods": "Mail, In-Person",
        "Acceptable Excuses": [
            "Public service of the U.S. or Delaware",
            "Spouse or dependent of person in public service",
            "U.S. citizen temporarily residing outside U.S.",
            "Sick or physically disabled",
            "Absent from district while on vacation",
            "Religious tenets",
            "Working hours and commutes",
            "Caregiver to a sick or disabled person"
        ],
        "ID or Other Requirements": "No ID required to request an absentee ballot."
    },
    {
        "State": "Florida",
        "Excuse Required": "No",
        "Application Deadline": "Received 10 days before Election Day",
        "Submission Methods": "Mail, Online, In-Person",
        "Acceptable Excuses": "Not applicable; no excuse required.",
        "ID or Other Requirements": "No ID required to request an absentee ballot; however, the voter's signature on the ballot certificate is verified against the signature on file."
    },
    {
        "State": "Georgia",
        "Excuse Required": "No",
        "Application Deadline": "Received 11 days before Election Day",
        "Submission Methods": "Mail, Online, In-Person",
        "Acceptable Excuses": "Not applicable; no excuse required.",
        "ID or Other Requirements": "No ID required to request an absentee ballot; however, the voter's signature on the ballot envelope is verified against the signature on file."
    },
    {
        "State": "Hawaii",
        "Excuse Required": "No",
        "Application Deadline": "Received 7 days before Election Day",
        "Submission Methods": "Mail, Online, In-Person",
        "Acceptable Excuses": "Not applicable; no excuse required.",
        "ID or Other Requirements": "No ID required to request or submit an absentee ballot."
    },
    {
        "State": "Idaho",
        "Excuse Required": "No",
        "Application Deadline": "Received 11 days before Election Day",
        "Submission Methods": "Mail, Online, In-Person",
        "Acceptable Excuses": "Not applicable; no excuse required.",
        "ID or Other Requirements": "No ID required to request an absentee ballot; however, the voter's signature on the absentee ballot affidavit is verified against the signature on file."
    },
    {
        "State": "Illinois",
        "Excuse Required": "No",
        "Application Deadline": "Received 5 days before Election Day",
        "Submission Methods": "Mail, Online, In-Person",
        "Acceptable Excuses": "Not applicable; no excuse required.",
        "ID or Other Requirements": "No ID required to request an absentee ballot; however, first-time voters who registered by mail may need to provide ID."
    },
    {
        "State": "Indiana",
        "Excuse Required": "Yes",
        "Application Deadline": "Received 12 days before Election Day",
        "Submission Methods": "Mail, In-Person",
        "Acceptable Excuses": [
            "Being out of the county on Election Day",
            "Illness or injury",
            "Caring for an individual confined due to illness or injury",
            "Disability",
            "65 years of age or older",
            "Scheduled to work during the entire 12 hours that polls are open",
            "Election duties outside of your precinct",
            "Observing a religious discipline or holiday during the entire 12 hours that polls are open",
            "Being a participant in the address confidentiality program",
            "Being a member of the military or public safety officer"
        ],
        "ID or Other Requirements": "No ID required to request an absentee ballot; however, the voter's signature on the absentee ballot application is verified against the signature on file."
    },
    {
        "State": "Iowa",
        "Excuse Required": "No",
        "Application Deadline": "Received 15 days before Election Day",
        "Submission Methods": "Mail, Online, In-Person",
        "Acceptable Excuses": "Not applicable; no excuse required.",
        "ID or Other Requirements": "Voter ID number (Iowa driver's license or non-operator ID number) or voter PIN is required when requesting an absentee ballot."
    },
    {
        "State": "Kansas",
        "Excuse Required": "No",
        "Application Deadline": "Received 7 days before Election Day",
        "Submission Methods": "Mail, Online, In-Person",
        "Acceptable Excuses": "Not applicable; no excuse required.",
        "ID or Other Requirements": "Voter's signature on the absentee ballot application is verified against the signature on file."
    },
    {
        "State": "Kentucky",
        "Excuse Required": "Yes",
        "Application Deadline": "Received 7 days before Election Day",
        "Submission Methods": "Mail, Online, In-Person",
        "Acceptable Excuses": [
            "Advanced age, disability, or illness",
            "Military personnel, their dependents, or overseas citizens",
            "Student who temporarily resides outside the county",
            "A voter who temporarily resides outside of Kentucky and who maintains eligibility to vote in Kentucky, such as a 'snowbird'",
            "Incarcerated but not yet convicted",
            "Employment that takes you out of the county all hours the polling place is open",
            "Participant in the address confidentiality program"
        ],
        "ID or Other Requirements": "No ID required to request an absentee ballot; however, the voter's signature on the absentee ballot application is verified against the signature on file."
    },
    {
        "State": "Louisiana",
        "Excuse Required": "Yes",
        "Application Deadline": "Received 4 days before Election Day",
        "Submission Methods": "Mail, Online, In-Person",
        "Acceptable Excuses": [
            "Senior citizen aged 65 or older",
            "Student, instructor, or professor located and living outside of your parish",
            "Clergy member assigned outside of your parish",
            "Temporarily outside of your parish or state",
            "Moved to a new parish more than 100 miles from your old parish after the registration books closed",
            "Involuntary confinement in an institution",
            "Hospitalized",
            "Offshore worker",
            "Person with a disability",
            "Sequestered jury member"
        ],
        "ID or Other Requirements": "No ID required to request an absentee ballot; however, the voter's signature on the absentee ballot application is verified against the signature on file."
    },
    {
        "State": "Maine",
        "Excuse Required": "No",
        "Application Deadline": "Received 3 days before Election Day",
        "Submission Methods": "Mail, In-Person",
        "Acceptable Excuses": "Not applicable; no excuse required.",
        "ID or Other Requirements": "No ID required to request an absentee ballot; however, first-time voters who registered by mail may need to provide ID."
    },
    {
        "State": "Maryland",
        "Excuse Required": "No",
        "Application Deadline": "Received 7 days before Election Day",
        "Submission Methods": "Mail, Online, In-Person",
        "Acceptable Excuses": "Not applicable; no excuse required.",
        "ID or Other Requirements": "No ID required to request an absentee ballot; however, first-time voters who registered by mail may need to provide ID."
    },
    {
        "State": "Massachusetts",
        "Excuse Required": "No",
        "Application Deadline": "Received 4 days before Election Day",
        "Submission Methods": "Mail, Online, In-Person",
        "Acceptable Excuses": "Not applicable; no excuse required.",
        "ID or Other Requirements": "No ID required to request an absentee ballot; however, first-time voters who registered by mail may need to provide ID."
    },
    {
        "State": "Michigan",
        "Excuse Required": "No",
        "Application Deadline": "Received by 5 PM the Friday before Election Day",
        "Submission Methods": "Mail, Online, In-Person",
        "Acceptable Excuses": "Not applicable; no excuse required.",
        "ID or Other Requirements": "No ID required to request an absentee ballot; however, first-time voters who registered by mail may need to provide ID."
    },
    {
        "State": "Minnesota",
        "Excuse Required": "No",
        "Application Deadline": "Received 1 day before Election Day",
        "Submission Methods": "Mail, Online, In-Person",
        "Acceptable Excuses": "Not applicable; no excuse required.",
        "ID or Other Requirements": "No ID required to request an absentee ballot; however, first-time voters who registered by mail may need to provide ID."
    },
    {
        "State": "Mississippi",
        "Excuse Required": "Yes",
        "Application Deadline": "Received by noon, 3 days before Election Day",
        "Submission Methods": "Mail, In-Person",
        "Acceptable Excuses": [
            "Being away from your county on Election Day for any reason",
            "Being a student, teacher, or administrator at a school whose studies or employment there necessitates absence from the county on Election Day",
            "Being required to be at work on Election Day during the times at which the polls will be open",
            "Being disabled",
            "Being 65 years of age or older",
            "Being a parent, spouse, or dependent of a person with a disability who is hospitalized outside of their county of residence or more than 50 miles away and you will be with that person on Election Day",
            "Being a member of the Mississippi congressional delegation, or spouse or dependent of such member"
        ],
        "ID or Other Requirements": "A copy of an acceptable photo ID must be submitted with the absentee ballot application."
    },
    {
        "State": "Missouri",
        "Excuse Required": "Yes",
        "Application Deadline": "Received by 5 PM, 2 Wednesdays before Election Day",
        "Submission Methods": "Mail, In-Person",
        "Acceptable Excuses": [
            "Absence on Election Day from the jurisdiction of the election authority in which you are registered to vote",
            "Incapacity or confinement due to illness or physical disability, including caring for a person who is incapacitated or confined due to illness or disability",
            "Religious belief or practice",
            "Employment as an election authority, as a member of an election authority, or by an election authority at a location other than your polling place",
            "Incarceration, provided all qualifications for voting are retained",
            "Certified participation in the address confidentiality program"
        ],
        "ID or Other Requirements": "A copy of an acceptable photo ID must be submitted with the absentee ballot application."
    },
    {
        "State": "Montana",
        "Excuse Required": "No",
        "Application Deadline": "Received by noon the day before Election Day",
        "Submission Methods": "Mail, In-Person",
        "Acceptable Excuses": "Not applicable; no excuse required.",
        "ID or Other Requirements": "No ID required to request an absentee ballot; however, first-time voters who registered by mail and did not provide ID will need to provide a copy of ID with their ballot."
    },
    {
        "State": "Nebraska",
        "Excuse Required": "No",
        "Application Deadline": "Received by close of business, 2nd Friday before Election Day",
        "Submission Methods": "Mail, In-Person",
        "Acceptable Excuses": "Not applicable; no excuse required.",
        "ID or Other Requirements": "No ID required to request an absentee ballot; however, first-time voters who registered by mail and did not provide ID will need to provide a copy of ID with their ballot."
    },
    {
        "State": "Nevada",
        "Excuse Required": "No",
        "Application Deadline": "Received 14 days before Election Day",
        "Submission Methods": "Mail, Online, In-Person",
        "Acceptable Excuses": "Not applicable; no excuse required.",
        "ID or Other Requirements": "No ID required to request an absentee ballot; however, the voter's signature on the absentee ballot return envelope is verified against the signature on file."
    },
    {
        "State": "New Hampshire",
        "Excuse Required": "Yes",
        "Application Deadline": "Received by 5 PM the day before Election Day",
        "Submission Methods": "Mail, In-Person",
        "Acceptable Excuses": [
            "Planned absence from city/town on Election Day",
            "Religious observance",
            "Disability",
            "Employment obligations, including care of children and infirm adults, during polling hours"
        ],
        "ID or Other Requirements": "No ID required to request an absentee ballot; however, the voter's signature on the absentee ballot affidavit is verified against the signature on file."
    },
    {
        "State": "New Jersey",
        "Excuse Required": "No",
        "Application Deadline": "Received 7 days before Election Day",
        "Submission Methods": "Mail, In-Person",
        "Acceptable Excuses": "Not applicable; no excuse required.",
        "ID or Other Requirements": "No ID required to request an absentee ballot; however, first-time voters who registered by mail and did not provide ID will need to provide a copy of ID with their ballot."
    },
    {
        "State": "New Mexico",
        "Excuse Required": "No",
        "Application Deadline": "Received by 5 PM, Thursday before Election Day",
        "Submission Methods": "Mail, Online, In-Person",
        "Acceptable Excuses": "Not applicable; no excuse required.",
        "ID or Other Requirements": "No ID required to request an absentee ballot; however, first-time voters who registered by mail and did not provide ID will need to provide a copy of ID with their ballot."
    },
    {
        "State": "New York",
        "Excuse Required": "Yes",
        "Application Deadline": "Received 15 days before Election Day",
        "Submission Methods": "Mail, Online, In-Person",
        "Acceptable Excuses": [
            "Absence from county or New York City on Election Day",
            "Temporary illness or physical disability",
            "Permanent illness or physical disability",
            "Primary caregiver of one or more individuals who are ill or physically disabled",
            "Resident or patient of a Veterans Health Administration Hospital",
            "Detained in jail awaiting Grand Jury action or confined in prison after conviction for an offense other than a felony"
        ],
        "ID or Other Requirements": "No ID required to request an absentee ballot; however, the voter's signature on the absentee ballot envelope is verified against the signature on file."
    },
    {
        "State": "North Carolina",
        "Excuse Required": "No",
        "Application Deadline": "Received by 5 PM, Tuesday before Election Day",
        "Submission Methods": "Mail, Online, In-Person",
        "Acceptable Excuses": "Not applicable; no excuse required.",
        "ID or Other Requirements": "A copy of an acceptable photo ID must be submitted with the absentee ballot request form."
    },
    {
        "State": "North Dakota",
        "Excuse Required": "No",
        "Application Deadline": "Received the day before Election Day",
        "Submission Methods": "Mail, Online, In-Person",
        "Acceptable Excuses": "Not applicable; no excuse required.",
        "ID or Other Requirements": "Voter's ID number (North Dakota driver's license, non-driver ID, or tribal ID) is required when requesting an absentee ballot."
    },
    {
        "State": "Ohio",
        "Excuse Required": "No",
        "Application Deadline": "Received by noon, 3 days before Election Day",
        "Submission Methods": "Mail, In-Person",
        "Acceptable Excuses": "Not applicable; no excuse required.",
        "ID or Other Requirements": "Voter's Ohio driver's license number, last four digits of Social Security number, or a copy of an acceptable photo ID must be submitted with the absentee ballot application."
    },
    {
        "State": "Oklahoma",
        "Excuse Required": "No",
        "Application Deadline": "Received by 5 PM, Tuesday before Election Day",
        "Submission Methods": "Mail, Online, In-Person",
        "Acceptable Excuses": "Not applicable; no excuse required.",
        "ID or Other Requirements": "No ID required to request an absentee ballot; however, the voter's signature on the absentee ballot affidavit must be notarized or witnessed by two people."
    },
    {
        "State": "Oregon",
        "Excuse Required": "No",
        "Application Deadline": "N/A (All-mail voting state)",
        "Submission Methods": "Mail, In-Person",
        "Acceptable Excuses": "Not applicable; no excuse required.",
        "ID or Other Requirements": "No ID required to request an absentee ballot; however, the voter's signature on the return envelope is verified against the signature on file."
    },
    {
        "State": "Pennsylvania",
        "Excuse Required": "No",
        "Application Deadline": "Received by 5 PM, Tuesday before Election Day",
        "Submission Methods": "Mail, Online, In-Person",
        "Acceptable Excuses": "Not applicable; no excuse required.",
        "ID or Other Requirements": "Voter's Pennsylvania driver's license number, PennDOT ID number, or last four digits of Social Security number must be provided when requesting an absentee ballot."
    },
    {
        "State": "Rhode Island",
        "Excuse Required": "No",
        "Application Deadline": "Received 21 days before Election Day",
        "Submission Methods": "Mail, In-Person",
        "Acceptable Excuses": "Not applicable; no excuse required.",
        "ID or Other Requirements": "No ID required to request an absentee ballot; however, the voter's signature on the return envelope is verified against the signature on file."
    },
    {
        "State": "South Carolina",
        "Excuse Required": "Yes",
        "Application Deadline": "Received by 5 PM, 11 days before Election Day",
        "Submission Methods": "Mail, In-Person",
        "Acceptable Excuses": [
            "Being on vacation outside your county of residence on Election Day",
            "Being a student attending school outside your county of residence",
            "Being 65 years of age or older",
            "Having a physical disability",
            "Being a member of the Armed Forces or Merchant Marine, a spouse or dependent residing with them",
            "Being admitted to the hospital as an emergency patient on Election Day or within a four-day period before the election",
            "Having a death or funeral in the family within three days before the election",
            "Being confined to a jail or pre-trial facility pending disposition of arrest or trial",
            "Being employed during polling hours on Election Day"
        ],
        "ID or Other Requirements": "A copy of an acceptable photo ID must be submitted with the absentee ballot application."
    },
    {
        "State": "South Dakota",
        "Excuse Required": "No",
        "Application Deadline": "Received by 5 PM the day before Election Day",
        "Submission Methods": "Mail, In-Person",
        "Acceptable Excuses": "Not applicable; no excuse required.",
        "ID or Other Requirements": "Voter's South Dakota driver's license number or a copy of an acceptable photo ID must be submitted with the absentee ballot application."
    },
    {
        "State": "Tennessee",
        "Excuse Required": "Yes",
        "Application Deadline": "Received 7 days before Election Day",
        "Submission Methods": "Mail, In-Person",
        "Acceptable Excuses": [
            "Being outside the county of registration during the early voting period and on Election Day",
            "Being enrolled as a full-time student (or spouse of such a student) at an institution outside the county of registration",
            "Being hospitalized, ill, or physically disabled",
            "Being a caretaker of a person who is hospitalized, ill, or physically disabled",
            "Being 60 years of age or older",
            "Being unable to appear at the polling place due to observance of a religious holiday",
            "Serving as an election official or a member or employee of the election commission",
            "Being a candidate for office in the election",
            "Serving on jury duty in a state or federal court",
            "Being a voter with a disability and whose polling place is inaccessible"
        ],
        "ID or Other Requirements": "A copy of an acceptable photo ID must be submitted with the absentee ballot application."
    },
    {
        "State": "Texas",
        "Excuse Required": "Yes",
        "Application Deadline": "Received by close of business, 11 days before Election Day",
        "Submission Methods": "Mail, In-Person",
        "Acceptable Excuses": [
            "Being 65 years of age or older",
            "Being disabled",
            "Being out of the county on Election Day and during the early voting period",
            "Being confined in jail but otherwise eligible to vote"
        ],
        "ID or Other Requirements": "Voter's Texas driver's license number, personal ID number, or last four digits of Social Security number must be provided when requesting an absentee ballot."
    },
    {
        "State": "Utah",
        "Excuse Required": "No",
        "Application Deadline": "Received 11 days before Election Day",
        "Submission Methods": "Mail, Online, In-Person",
        "Acceptable Excuses": "Not applicable; no excuse required.",
        "ID or Other Requirements": "No ID required to request an absentee ballot; however, first-time voters who did not provide ID when registering may need to provide ID when voting."
    },
    {
        "State": "Vermont",
        "Excuse Required": "No",
        "Application Deadline": "Received by 5 PM the day before Election Day",
        "Submission Methods": "Mail, Online, In-Person",
        "Acceptable Excuses": "Not applicable; no excuse required.",
        "ID or Other Requirements": "No ID required to request an absentee ballot; however, first-time voters who did not provide ID when registering may need to provide ID when voting."
    },
    {
        "State": "Virginia",
        "Excuse Required": "No",
        "Application Deadline": "Received by 5 PM, 11 days before Election Day",
        "Submission Methods": "Mail, Online, In-Person",
        "Acceptable Excuses": "Not applicable; no excuse required.",
        "ID or Other Requirements": "No ID required to request an absentee ballot; however, first-time voters who did not provide ID when registering may need to provide ID when voting."
    },
    {
        "State": "Washington",
        "Excuse Required": "No",
        "Application Deadline": "N/A (All-mail voting state)",
        "Submission Methods": "Mail, In-Person",
        "Acceptable Excuses": "Not applicable; no excuse required.",
        "ID or Other Requirements": "No ID required to request an absentee ballot; however, first-time voters who did not provide ID when registering may need to provide ID when voting."
    },
    {
        "State": "West Virginia",
        "Excuse Required": "Yes",
        "Application Deadline": "Received 6 days before Election Day",
        "Submission Methods": "Mail, In-Person",
        "Acceptable Excuses": [
            "Illness, injury, or other medical reason",
            "Disability or advanced age",
            "Incarceration or home detention (not for felony)",
            "Work hours and distance from county seat",
            "Inaccessible early voting site and polling place",
            "Personal or business travel",
            "Attendance at college or other place of education or training",
            "Temporary residence outside of the county",
            "Service as an elected or appointed state or federal official"
        ],
        "ID or Other Requirements": "No ID required to request an absentee ballot; however, the voter's signature on the absentee ballot application is verified against the signature on file."
    },
    {
        "State": "Wisconsin",
        "Excuse Required": "No",
        "Application Deadline": "Received by 5 PM, Thursday before Election Day",
        "Submission Methods": "Mail, Online, In-Person",
        "Acceptable Excuses": "Not applicable; no excuse required.",
        "ID or Other Requirements": "A copy of an acceptable photo ID must be submitted with the absentee ballot application."
    },
    {
        "State": "Wyoming",
        "Excuse Required": "No",
        "Application Deadline": "Received by 5 PM the day before Election Day",
        "Submission Methods": "Mail, In-Person",
        "Acceptable Excuses": "Not applicable; no excuse required.",
        "ID or Other Requirements": "No ID required to request an absentee ballot; however, first-time voters who did not provide ID when registering may need to provide ID when voting."
    }
]


# Define the CSV file name
csv_file = 'absentee_voting_requirements.csv'

# Field names for the CSV file
fieldnames = ["State", "Excuse Required", "Application Deadline", "Submission Methods", "Acceptable Excuses", "ID or Other Requirements"]

# Write the data to the CSV file
with open(csv_file, mode='w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    
    for entry in absentee_requirements:
        # Flatten "Acceptable Excuses" list to a single string
        entry["Acceptable Excuses"] = "; ".join(entry["Acceptable Excuses"]) if isinstance(entry["Acceptable Excuses"], list) else entry["Acceptable Excuses"]
        writer.writerow(entry)

print(f'Data has been written to {csv_file}')
