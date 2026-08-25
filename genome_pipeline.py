# ============================================
# PART A — Toolkit Functions
# ============================================

def get_gc(seq):
    return round ((seq.count("G") + seq.count("C")) /len(seq) * 100, 2 )

def classify_gc(seq):
    gc = get_gc(seq)
    if gc >= 70:
        category =  "high gc"
    elif gc >= 50:
        category = "medium gc"
    else:
        category =  "low gc"
    return category

def get_complement(seq):
    complement = ""
    for base in seq:
        if base == "A":
            complement += "T"
        elif base =="T":
            complement += "A"
        elif base == "G":
            complement += "C"
        elif base == "C":
            complement += "G"
    return complement 

def is_valid(seq):
    for base in seq:
        if base not in "ATGC":
            return False
    return True

def get_freq(seq):
    freq = {}
    for base in seq:
        freq[base] = freq.get(base, 0) +1
    return freq

# ============================================
# PART B — File Handling
# ============================================

def parse_fasta(filename):
    
    try:
        sequences = {}
        with open (filename, "r") as f :
            for line in f:
                line = line.strip()

# skip empty lines in FASTA file

                if not line:
                    continue

                if line.startswith(">"):

# remove > from header line

                    header = line[1:]
                    sequences[header] = ""
                else:
                    sequences[header] += line 
        return sequences

    except FileNotFoundError as e:
        print (f"Error: {e}")
        return {}

# ============================================
# PART C — Validation
# ============================================

def validate_seq(seq):
    if not seq:
        print("Error: empty, no sequence")
        return False

    if not all (base in "ATGC" for base in seq):
        print("invalid character")
        return False

    if len(seq) < 6:
        print("seq length too short")
        return False
    return True

# ============================================
# PART D — Analysis
# ============================================

def analyze_sequence(name, seq):
    gc = get_gc(seq)
    complement = get_complement(seq)
    cat = classify_gc(seq)
    valid = is_valid(seq)
    freq = get_freq(seq)

    reports  = {
        "name": name,
        "sequence": seq,
        "length": len(seq),
        "gc": gc,
        "category": cat,
        "complement": complement,
        "valid": valid,
        "frequency": freq
 }
    return reports

# ============================================
# PART E — Report Writer
# ============================================

def write_report(reports, output_file):
    with open(output_file,  "w") as f :
        for report in reports :
            f.write(f"Gene:  {report['name']}\n")
            f.write(f"Sequence:  {report['sequence']}\n")
            f.write(f"Length:  {report['length']}\n")
            f.write(f"validity:  {report['valid']}\n")
            f.write(f"GC%:  {report['gc']}\n")
            f.write(f"Category:  {report['category']}\n")
            f.write(f"Complementary Sequence:  {report['complement']}\n")
            f.write(f"frequency of bases:  {report['frequency']}\n")
            f.write("-"* 40 + "\n")

        if reports:
            best = max(reports, key= lambda r: r["gc"])
            f.write(f"Highest GC: {best['name']} at {best['gc']}%\n")            


# ============================================
# PART F — Main Pipeline
# ============================================

def run_pipeline(input_file, output_file):
    sequences = parse_fasta(input_file)

    results = []
    valid_count  =0 
    total = len(sequences)

    for name, seq in sequences.items():

        if not validate_seq (seq):
            continue 

        result = analyze_sequence(name, seq)
        results.append(result)
        valid_count += 1 

    write_report(results, output_file)

    total_gc = 0
    for result in results:
        total_gc += result["gc"]

# only calculate average if there are valid sequences

    if valid_count > 0:    
        average_gc = total_gc / valid_count
        best = max(results, key = lambda r:r ["gc"])

        print("Total sequences:", total)
        print("Valid sequences:", valid_count)
        print("Average GC%:", round(average_gc, 2))
        print("Highest GC gene:", best["name"])
        print("Highest GC%:", best["gc"])
    else:
        print("No valid sequences.")

# ============================================
# RUN
# ============================================

run_pipeline("sequences.fasta.txt", "report.txt")
