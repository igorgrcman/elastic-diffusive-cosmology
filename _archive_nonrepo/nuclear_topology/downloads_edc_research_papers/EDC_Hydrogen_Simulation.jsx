import React, { useState, useEffect, useCallback } from 'react';

// EDC Constants
const ALPHA = 1/137.036;
const R_E = 2.818e-15;  // topological scale (m)
const A_0 = R_E / (ALPHA * ALPHA);  // Bohr radius
const R_XI = 2.16e-18;  // membrane thickness (m)

// Visualization scaling
const SCALE = 400 / A_0;  // pixels per Bohr radius
const CENTER_X = 400;
const CENTER_Y = 300;

// Energy calculations in eV
const E_RYDBERG = 13.6;  // eV

const EDCSimulation = () => {
  // State
  const [mode, setMode] = useState('single');  // 'single' or 'molecule'
  const [protonSeparation, setProtonSeparation] = useState(3.0);  // in units of a₀
  const [showBulk, setShowBulk] = useState(true);
  const [showFluxTubes, setShowFluxTubes] = useState(true);
  const [showEnergyPlot, setShowEnergyPlot] = useState(true);
  const [animating, setAnimating] = useState(false);
  const [time, setTime] = useState(0);

  // Animation
  useEffect(() => {
    if (animating) {
      const interval = setInterval(() => {
        setTime(t => t + 0.05);
        if (mode === 'molecule') {
          setProtonSeparation(d => {
            const newD = d - 0.02;
            if (newD <= 1.0) {
              setAnimating(false);
              return 1.4;  // equilibrium
            }
            return newD;
          });
        }
      }, 50);
      return () => clearInterval(interval);
    }
  }, [animating, mode]);

  // Calculate energies for H atom
  const calcHydrogenEnergy = (r) => {
    // r in units of a₀
    const kinetic = E_RYDBERG / (r * r);  // K ~ 1/r²
    const potential = -2 * E_RYDBERG / r;  // U ~ -1/r
    return { kinetic, potential, total: kinetic + potential };
  };

  // Calculate energies for H₂ molecule
  const calcH2Energy = (d) => {
    // d = proton separation in units of a₀
    // Simplified model based on our derivation
    
    if (d > 4) {
      // Two isolated atoms
      return { total: -2 * E_RYDBERG, binding: 0, electronDepth: 0 };
    }
    
    // Proton-proton repulsion
    const U_pp = 2 * E_RYDBERG / d;
    
    // Electron-proton attractions (each electron sees both protons)
    // Simplified: electrons at center, distance d/2 from each proton
    const r_ep = d / 2;
    const U_ep = -4 * (2 * E_RYDBERG / r_ep);  // 4 pairs, each -2E_R/r
    
    // Electron-electron repulsion (electrons separated by ~a₀)
    const r_ee = Math.max(0.5, d / 2);
    const U_ee = 2 * E_RYDBERG / r_ee;
    
    // Kinetic energy (electrons delocalized over larger region)
    const effectiveSize = Math.max(1, d / 2);
    const K = 2 * E_RYDBERG / (effectiveSize * effectiveSize);
    
    // Total
    const total = K + U_pp + U_ep + U_ee;
    
    // Electron depth in Bulk (from our derivation)
    // w* = sqrt(a₀² - (d/2)²) when flux tubes meet
    let electronDepth = 0;
    if (d < 2) {
      electronDepth = Math.sqrt(Math.max(0, 1 - (d/2) * (d/2))) * 0.71;
    }
    
    return { 
      total, 
      binding: total - (-2 * E_RYDBERG),
      electronDepth,
      U_pp,
      U_ep,
      U_ee,
      K
    };
  };

  // Generate energy curve data
  const generateEnergyCurve = () => {
    const points = [];
    for (let d = 0.5; d <= 5; d += 0.1) {
      const energy = mode === 'single' 
        ? calcHydrogenEnergy(d)
        : calcH2Energy(d);
      points.push({ d, energy: energy.total });
    }
    return points;
  };

  const energyCurve = generateEnergyCurve();
  const currentEnergy = mode === 'single' 
    ? calcHydrogenEnergy(1)  // at a₀
    : calcH2Energy(protonSeparation);

  // Render proton
  const Proton = ({ x, y, label }) => (
    <g>
      <circle cx={x} cy={y} r={12} fill="#e74c3c" stroke="#c0392b" strokeWidth={2} />
      <text x={x} y={y + 4} textAnchor="middle" fill="white" fontSize="10" fontWeight="bold">
        {label || 'P'}
      </text>
    </g>
  );

  // Render electron (as wave)
  const Electron = ({ x, y, bulkDepth = 0, spread = 30 }) => {
    const wavePoints = [];
    for (let i = 0; i <= 20; i++) {
      const angle = (i / 20) * Math.PI * 2;
      const wobble = Math.sin(angle * 3 + time * 5) * 5;
      const r = spread + wobble;
      wavePoints.push(`${x + r * Math.cos(angle)},${y + r * Math.sin(angle)}`);
    }
    
    return (
      <g>
        {/* Electron cloud */}
        <ellipse 
          cx={x} 
          cy={y + bulkDepth * 50} 
          rx={spread} 
          ry={spread * (1 - bulkDepth * 0.3)}
          fill="rgba(52, 152, 219, 0.3)" 
          stroke="#3498db" 
          strokeWidth={2}
        />
        {/* Core */}
        <circle 
          cx={x} 
          cy={y + bulkDepth * 50} 
          r={8} 
          fill="#3498db" 
        />
        <text 
          x={x} 
          y={y + bulkDepth * 50 + 3} 
          textAnchor="middle" 
          fill="white" 
          fontSize="8" 
          fontWeight="bold"
        >
          e⁻
        </text>
      </g>
    );
  };

  // Render flux tube
  const FluxTube = ({ x1, y1, x2, y2, bulkDepth = 0 }) => {
    if (!showFluxTubes) return null;
    
    // Flux tube goes through Bulk (curves down)
    const midX = (x1 + x2) / 2;
    const midY = (y1 + y2) / 2 + bulkDepth * 50;
    
    return (
      <path
        d={`M ${x1} ${y1} Q ${midX} ${midY} ${x2} ${y2}`}
        stroke="#27ae60"
        strokeWidth={3}
        fill="none"
        strokeDasharray={bulkDepth > 0 ? "5,5" : "none"}
        opacity={0.8}
      />
    );
  };

  // Render membrane line
  const Membrane = () => (
    <g>
      <line x1={50} y1={CENTER_Y} x2={750} y2={CENTER_Y} stroke="#95a5a6" strokeWidth={2} strokeDasharray="10,5" />
      <text x={60} y={CENTER_Y - 10} fill="#7f8c8d" fontSize="12">3D Membrane (w=0)</text>
    </g>
  );

  // Render Bulk region
  const BulkRegion = () => {
    if (!showBulk) return null;
    return (
      <g>
        <rect x={50} y={CENTER_Y} width={700} height={200} fill="rgba(155, 89, 182, 0.1)" />
        <text x={60} y={CENTER_Y + 180} fill="#8e44ad" fontSize="12">5D Bulk (w &gt; 0)</text>
      </g>
    );
  };

  // Energy plot
  const EnergyPlot = () => {
    if (!showEnergyPlot) return null;
    
    const plotX = 550;
    const plotY = 50;
    const plotW = 200;
    const plotH = 150;
    
    const minE = -35;
    const maxE = 20;
    const minD = 0.5;
    const maxD = 5;
    
    const scaleX = (d) => plotX + (d - minD) / (maxD - minD) * plotW;
    const scaleY = (e) => plotY + plotH - (e - minE) / (maxE - minE) * plotH;
    
    const pathD = energyCurve.map((p, i) => 
      `${i === 0 ? 'M' : 'L'} ${scaleX(p.d)} ${scaleY(p.energy)}`
    ).join(' ');
    
    const currentD = mode === 'single' ? 1 : protonSeparation;
    const currentE = currentEnergy.total;
    
    return (
      <g>
        {/* Background */}
        <rect x={plotX} y={plotY} width={plotW} height={plotH} fill="white" stroke="#bdc3c7" />
        
        {/* Zero line */}
        <line x1={plotX} y1={scaleY(0)} x2={plotX + plotW} y2={scaleY(0)} stroke="#bdc3c7" strokeDasharray="3,3" />
        
        {/* -27.2 eV line (2 × H atoms) */}
        {mode === 'molecule' && (
          <line x1={plotX} y1={scaleY(-27.2)} x2={plotX + plotW} y2={scaleY(-27.2)} stroke="#e74c3c" strokeDasharray="3,3" />
        )}
        
        {/* Energy curve */}
        <path d={pathD} stroke="#3498db" strokeWidth={2} fill="none" />
        
        {/* Current point */}
        <circle cx={scaleX(currentD)} cy={scaleY(currentE)} r={6} fill="#e74c3c" />
        
        {/* Labels */}
        <text x={plotX + plotW/2} y={plotY - 5} textAnchor="middle" fontSize="11" fontWeight="bold">
          Energy vs Distance
        </text>
        <text x={plotX + plotW + 5} y={plotY + plotH} fontSize="10">d/a₀</text>
        <text x={plotX - 5} y={plotY + 5} fontSize="10" textAnchor="end">E(eV)</text>
        
        {/* Current energy value */}
        <text x={plotX + plotW/2} y={plotY + plotH + 20} textAnchor="middle" fontSize="11">
          E = {currentE.toFixed(1)} eV
        </text>
      </g>
    );
  };

  // Single H atom view
  const SingleAtomView = () => {
    const energy = calcHydrogenEnergy(1);
    
    return (
      <g>
        <Proton x={CENTER_X} y={CENTER_Y} label="P" />
        <FluxTube x1={CENTER_X} y1={CENTER_Y} x2={CENTER_X + 80} y2={CENTER_Y} />
        <Electron x={CENTER_X + 80} y={CENTER_Y} spread={40} />
        
        {/* Labels */}
        <text x={CENTER_X} y={CENTER_Y + 40} textAnchor="middle" fontSize="12" fill="#7f8c8d">
          Proton (Y-junction)
        </text>
        <text x={CENTER_X + 80} y={CENTER_Y + 60} textAnchor="middle" fontSize="12" fill="#7f8c8d">
          Electron (standing wave)
        </text>
        
        {/* Distance marker */}
        <line x1={CENTER_X + 15} y1={CENTER_Y - 30} x2={CENTER_X + 65} y2={CENTER_Y - 30} stroke="#2c3e50" strokeWidth={1} markerEnd="url(#arrow)" markerStart="url(#arrow)" />
        <text x={CENTER_X + 40} y={CENTER_Y - 35} textAnchor="middle" fontSize="11" fill="#2c3e50">a₀</text>
        
        {/* Energy breakdown */}
        <g transform="translate(100, 400)">
          <text fontSize="13" fontWeight="bold" fill="#2c3e50">H Atom Energy:</text>
          <text y={20} fontSize="12" fill="#27ae60">Kinetic: +{energy.kinetic.toFixed(1)} eV</text>
          <text y={40} fontSize="12" fill="#e74c3c">Potential: {energy.potential.toFixed(1)} eV</text>
          <text y={60} fontSize="12" fill="#2c3e50" fontWeight="bold">Total: {energy.total.toFixed(1)} eV</text>
        </g>
      </g>
    );
  };

  // H₂ molecule view
  const MoleculeView = () => {
    const d = protonSeparation;
    const energy = calcH2Energy(d);
    const halfD = d * 40;  // scaled for display
    
    // Electron positions
    const electronX = CENTER_X;
    const electronBulkDepth = energy.electronDepth;
    
    return (
      <g>
        {/* Protons */}
        <Proton x={CENTER_X - halfD} y={CENTER_Y} label="P₁" />
        <Proton x={CENTER_X + halfD} y={CENTER_Y} label="P₂" />
        
        {/* Flux tubes */}
        <FluxTube 
          x1={CENTER_X - halfD} 
          y1={CENTER_Y} 
          x2={electronX} 
          y2={CENTER_Y} 
          bulkDepth={electronBulkDepth}
        />
        <FluxTube 
          x1={CENTER_X + halfD} 
          y1={CENTER_Y} 
          x2={electronX} 
          y2={CENTER_Y} 
          bulkDepth={electronBulkDepth}
        />
        
        {/* Electrons (shared) */}
        {d < 2.5 ? (
          // Shared electron cloud
          <Electron 
            x={electronX} 
            y={CENTER_Y} 
            bulkDepth={electronBulkDepth}
            spread={30 + (2.5 - d) * 10}
          />
        ) : (
          // Separate electrons
          <>
            <Electron x={CENTER_X - halfD + 50} y={CENTER_Y} spread={30} />
            <Electron x={CENTER_X + halfD - 50} y={CENTER_Y} spread={30} />
          </>
        )}
        
        {/* Distance marker */}
        <line 
          x1={CENTER_X - halfD} 
          y1={CENTER_Y - 40} 
          x2={CENTER_X + halfD} 
          y2={CENTER_Y - 40} 
          stroke="#2c3e50" 
          strokeWidth={1}
        />
        <text x={CENTER_X} y={CENTER_Y - 45} textAnchor="middle" fontSize="11" fill="#2c3e50">
          d = {d.toFixed(2)} a₀
        </text>
        
        {/* Bulk depth indicator */}
        {electronBulkDepth > 0 && showBulk && (
          <g>
            <line 
              x1={CENTER_X + 50} 
              y1={CENTER_Y} 
              x2={CENTER_X + 50} 
              y2={CENTER_Y + electronBulkDepth * 50}
              stroke="#8e44ad"
              strokeWidth={2}
              strokeDasharray="3,3"
            />
            <text 
              x={CENTER_X + 60} 
              y={CENTER_Y + electronBulkDepth * 25}
              fontSize="10"
              fill="#8e44ad"
            >
              w* = {(electronBulkDepth * 0.71).toFixed(2)} a₀
            </text>
          </g>
        )}
        
        {/* Energy breakdown */}
        <g transform="translate(80, 400)">
          <text fontSize="13" fontWeight="bold" fill="#2c3e50">H₂ Molecule Energy:</text>
          <text y={20} fontSize="11" fill="#2c3e50">Total: {energy.total.toFixed(1)} eV</text>
          <text y={38} fontSize="11" fill={energy.binding < 0 ? "#27ae60" : "#e74c3c"}>
            Binding: {energy.binding.toFixed(1)} eV {energy.binding < -4 && d < 2 ? "✓ Stable!" : ""}
          </text>
          <text y={56} fontSize="11" fill="#8e44ad">
            e⁻ in Bulk: {(electronBulkDepth * 38).toFixed(0)} pm
          </text>
          {d < 2 && (
            <text y={74} fontSize="10" fill="#7f8c8d">
              ({(electronBulkDepth * 38 / (R_XI * 1e12)).toExponential(1)} × R_ξ deep!)
            </text>
          )}
        </g>
      </g>
    );
  };

  return (
    <div className="p-4 bg-gray-100 min-h-screen">
      <h1 className="text-2xl font-bold text-center mb-4 text-gray-800">
        EDC 5D Simulation: Hydrogen Atom & H₂ Molecule
      </h1>
      
      {/* Controls */}
      <div className="flex flex-wrap gap-4 mb-4 justify-center">
        <div className="flex gap-2">
          <button
            onClick={() => { setMode('single'); setAnimating(false); }}
            className={`px-4 py-2 rounded ${mode === 'single' ? 'bg-blue-600 text-white' : 'bg-white text-gray-700'}`}
          >
            H Atom
          </button>
          <button
            onClick={() => { setMode('molecule'); setProtonSeparation(3.0); setAnimating(false); }}
            className={`px-4 py-2 rounded ${mode === 'molecule' ? 'bg-blue-600 text-white' : 'bg-white text-gray-700'}`}
          >
            H₂ Molecule
          </button>
        </div>
        
        <div className="flex gap-2">
          <label className="flex items-center gap-1">
            <input type="checkbox" checked={showBulk} onChange={e => setShowBulk(e.target.checked)} />
            <span className="text-sm">Show Bulk</span>
          </label>
          <label className="flex items-center gap-1">
            <input type="checkbox" checked={showFluxTubes} onChange={e => setShowFluxTubes(e.target.checked)} />
            <span className="text-sm">Flux Tubes</span>
          </label>
          <label className="flex items-center gap-1">
            <input type="checkbox" checked={showEnergyPlot} onChange={e => setShowEnergyPlot(e.target.checked)} />
            <span className="text-sm">Energy Plot</span>
          </label>
        </div>
        
        {mode === 'molecule' && (
          <div className="flex gap-2 items-center">
            <span className="text-sm">Proton separation:</span>
            <input
              type="range"
              min="0.8"
              max="4"
              step="0.05"
              value={protonSeparation}
              onChange={e => setProtonSeparation(parseFloat(e.target.value))}
              className="w-32"
            />
            <span className="text-sm w-16">{protonSeparation.toFixed(2)} a₀</span>
            <button
              onClick={() => { setProtonSeparation(3.0); setAnimating(true); }}
              className="px-3 py-1 bg-green-600 text-white rounded text-sm"
            >
              ▶ Animate
            </button>
          </div>
        )}
      </div>
      
      {/* Main SVG */}
      <svg width="800" height="500" className="mx-auto bg-white rounded shadow">
        <defs>
          <marker id="arrow" markerWidth="10" markerHeight="10" refX="5" refY="5" orient="auto">
            <path d="M0,0 L10,5 L0,10 Z" fill="#2c3e50" />
          </marker>
        </defs>
        
        <BulkRegion />
        <Membrane />
        
        {mode === 'single' ? <SingleAtomView /> : <MoleculeView />}
        
        <EnergyPlot />
        
        {/* Legend */}
        <g transform="translate(50, 50)">
          <text fontSize="12" fontWeight="bold" fill="#2c3e50">Legend:</text>
          <circle cx={10} cy={20} r={6} fill="#e74c3c" />
          <text x={25} y={24} fontSize="11">Proton (flux source)</text>
          <circle cx={10} cy={40} r={6} fill="#3498db" />
          <text x={25} y={44} fontSize="11">Electron (flux sink)</text>
          <line x1={5} y1={60} x2={40} y2={60} stroke="#27ae60" strokeWidth={3} />
          <text x={50} y={64} fontSize="11">Flux tube</text>
        </g>
      </svg>
      
      {/* Info panel */}
      <div className="mt-4 p-4 bg-white rounded shadow max-w-3xl mx-auto">
        <h3 className="font-bold text-lg mb-2">
          {mode === 'single' ? 'Hydrogen Atom in EDC' : 'H₂ Molecule Formation in EDC'}
        </h3>
        {mode === 'single' ? (
          <div className="text-sm text-gray-700 space-y-2">
            <p><strong>Proton:</strong> Y-junction where 3 vortex lines meet. Acts as flux source.</p>
            <p><strong>Electron:</strong> Surface defect on membrane. Standing wave pattern. Acts as flux sink.</p>
            <p><strong>Flux tube:</strong> Connects proton and electron through 5D Bulk. Has tension τ = α⁵·σ_eff·r_e</p>
            <p><strong>Equilibrium (a₀):</strong> Balance between flux tube tension (wants shorter) and quantum pressure (resists compression).</p>
            <p><strong>Key result:</strong> a₀ = r_e/α² directly from 5D geometry!</p>
          </div>
        ) : (
          <div className="text-sm text-gray-700 space-y-2">
            <p><strong>Two H atoms approach:</strong> As d decreases, electrons begin to "see" both protons.</p>
            <p><strong>Shared electron cloud:</strong> At d ~ 2a₀, electrons form shared vibrational mode.</p>
            <p><strong>Electrons sink into Bulk:</strong> At equilibrium (d = 1.4a₀), electrons are w* = 0.71a₀ = 38 pm deep!</p>
            <p><strong>Revolutionary insight:</strong> Chemical bonds are 5D phenomena. Electrons in molecules are NOT on the 3D membrane!</p>
            <p><strong>Bond energy:</strong> ~4.5 eV comes from shorter total flux tube length in molecular configuration.</p>
          </div>
        )}
      </div>
    </div>
  );
};

export default EDCSimulation;
