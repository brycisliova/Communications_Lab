# EE340: Communications Lab Repository

### Course Information
- **Course:** EE340 - Communications Lab
- **Institute:** Wadhwani Electronics Lab, Department of Electrical Engineering, IIT Bombay
- **Platform:** GNU Radio

---

### Repository Overview

This repository contains experiment files, handouts, reports, and solutions for the EE340 Communications Lab. Each experiment is designed to enhance your understanding of communication systems and signal processing concepts using **GNU Radio**.

> **⚠️ Warning:**  
> In this repository, I have provided handouts, detailed reports, and solutions for each lab experiment. You’re welcome to refer to these materials, but I encourage you to at least attempt each lab on your own. Yes, it might seem convenient to directly use the solutions, and I understand that labs can sometimes feel repetitive. But trust me—working through each experiment, building the flow graphs, and relating these labs to **EE341: Communications Theory** brings an entirely different level of understanding and confidence.
>  
> Making these connections is rewarding in the long run, as it not only solidifies your grasp of communication principles but also benefits future courses and projects. Use this repository as a reference, not as a shortcut!  
>  
> If you have questions about any lab in this repository or any other related topics, feel free to reach out to me at **jatin.ee.iitb@gmail.com**.

---

## Table of Contents

1. [Introduction to GNU Radio](#introduction-to-gnu-radio)
2. [Lab Experiments](#lab-experiments)
   - [Lab 0: GNU Radio Basics](#lab-0-gnu-radio-basics)
   - [Lab 1: Music Synthesis and Audio Processing](#lab-1-music-synthesis-and-audio-processing)
   - [Lab 2: Amplitude Modulation (AM)](#lab-2-amplitude-modulation-am)
   - [Lab 3: Frequency Modulation (FM)](#lab-3-frequency-modulation-fm)
   - [Lab 4: Non-Linearity Effects in Communication Systems](#lab-4-non-linearity-effects-in-communication-systems)
   - [Lab 5: Pulse Shaping and Digital Transmission](#lab-5-pulse-shaping-and-digital-transmission)
   - [Lab 6 (Addendum): Matched Filtering and QPSK Modulation](#lab-6-addendum-matched-filtering-and-qpsk-modulation)
   - [Lab 7 (Addendum): Multipath Propagation and Equalization](#lab-7-addendum-multipath-propagation-and-equalization)
   - [Lab 8 (Addendum): Carrier Frequency and Phase Synchronization](#lab-8-addendum-carrier-frequency-and-phase-synchronization)
   - [Lab 9 (Addendum): End-to-End Communication](#lab-9-addendum-end-to-end-communication)
3. [Mid-Semester Exam](#mid-semester-exam)
4. [Resources](#resources)
5. [Installation Instructions](#installation-instructions)

---

## Introduction to GNU Radio
GNU Radio is an open-source toolkit providing a wide array of signal processing blocks for software-defined radios (SDRs) and simulation environments. It is extensively used in research, industry, and academia to study and implement wireless communication systems.

## Lab Experiments

Each lab experiment is intended to introduce and solidify different aspects of communication systems. Below is a brief summary of each lab:

### Lab 0: GNU Radio Basics
**Objective:** Familiarize yourself with the GNU Radio environment and GUI.  
**Summary:** Explore basic GNU Radio blocks, build simple flow graphs, and get hands-on with foundational signal processing concepts.

### Lab 1: Music Synthesis and Audio Processing
**Tasks:** Create melodies, mix audio, equalize frequencies, and apply denoising techniques.  
**Outcome:** Understand audio signal processing with practical tasks like synthesizing the “Happy Birthday” tune.

### Lab 2: Amplitude Modulation (AM)
**Tasks:** Implement DSB-FC & DSB-SC AM modulation, explore IQ signals, and visualize AM signals in time and frequency domains.  
**Outcome:** Gain hands-on experience with AM modulation and demodulation techniques.

### Lab 3: Frequency Modulation (FM)
**Tasks:** Generate FM signals, demodulate, and apply pre-emphasis/de-emphasis to mitigate high-frequency noise.  
**Outcome:** Learn FM modulation and demodulation with practical applications.

### Lab 4: Non-Linearity Effects in Communication Systems
**Tasks:** Analyze second- and third-order non-linearities and observe their effects on signal quality.  
**Outcome:** Develop an understanding of signal distortion due to non-linearities.

### Lab 5: Pulse Shaping and Digital Transmission
**Tasks:** Implement RRC filters, create BPSK symbols, and examine eye diagrams for ISI analysis.  
**Outcome:** Learn about pulse shaping, an essential technique in digital communication.

### Lab 6 (Addendum): Matched Filtering and QPSK Modulation
**Tasks:** Study noise effects on QPSK modulation and implement matched filtering for noise reduction.  
**Outcome:** Understand the role of matched filters in demodulation within noisy environments.

### Lab 7 (Addendum): Multipath Propagation and Equalization
**Tasks:** Model multipath propagation, add noise, and apply equalization techniques for error correction.  
**Outcome:** Learn to counter signal degradation in multipath channels through equalization.

### Lab 8 (Addendum): Carrier Frequency and Phase Synchronization
**Tasks:** Address frequency and phase offsets in QPSK using the Costas loop and Viterbi algorithm.  
**Outcome:** Gain insights into synchronization techniques in digital communication.

### Lab 9 (Addendum): End-to-End Communication
**Tasks:** Complete end-to-end data transmission using BPSK, DBPSK, and DQPSK, applying modulation and synchronization concepts.  
**Outcome:** Practice all prior techniques to achieve successful data transmission from end to end.

---

## Mid-Semester Exam

The Mid-Semester Exam covers core topics in modulation, phase, and frequency analysis:
- **Task 1:** Signal demodulation and message extraction, with a required flow diagram.
- **Task 2:** Analysis involving phase and frequency modulation, also with a flow diagram.
  
**Outcome:** Reinforces practical understanding of communication systems, especially the importance of clear diagrammatic representation in complex flow graphs.

---

## Resources

- **GNU Radio Installation Guide:** Refer to `docs/GNU_Radio_Installation.pdf`.
- **Sample Rate Reference:** Check individual lab instructions for sample rates.
- **Troubleshooting Guide:** Each lab folder contains notes and common issue resolutions.

---

## Installation Instructions

1. **Install GNU Radio:** Follow the official installation guide for GNU Radio.
2. **Clone this repository:**
   ```bash
   git clone https://github.com/brycisliova/Communications_Lab.git
   cd Communications_Lab
Run Lab Flowgraphs: Open the .grc files in GNU Radio Companion and execute the flowgraphs as per the instructions.
> **Note:**  
> This repository is intended for educational purposes. To fully benefit, follow each lab’s manual, observe results, and analyze different outcomes.
